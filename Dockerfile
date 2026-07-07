# =============================================================================
# NetVault NOC — Production Dockerfile
# Multi-stage build: python:3.11-slim base
# Tag: jorahone/netvault:latest
# =============================================================================

# ---- Build Stage ----
FROM python:3.11-slim AS builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user --upgrade pip && \
    pip install --no-cache-dir --user gunicorn && \
    pip install --no-cache-dir --user -r requirements.txt

# ---- Runtime Stage ----
FROM python:3.11-slim

# Create non-root user
RUN groupadd -r netvault && useradd -r -g netvault -d /app -s /sbin/nologin netvault

# Install runtime dependencies (rclone, ssh client for fabric/paramiko)
RUN apt-get update && apt-get install -y --no-install-recommends \
    rclone \
    openssh-client \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /root/.local /usr/local
COPY --from=builder /root/.local/bin /usr/local/bin

# Create application directories
RUN mkdir -p /app /data /config /var/lib/netvault/tftp /var/lib/netvault/configs /etc/netvault

# Copy application code
COPY . /app
WORKDIR /app

# Ensure config directory exists for default.conf
RUN mkdir -p /app/config

# Set ownership
RUN chown -R netvault:netvault /app /data /config /var/lib/netvault /etc/netvault

# Ensure data directory is writable
RUN mkdir -p /app/data && chmod 777 /app/data

# Switch to non-root user
USER netvault

# Expose application port
EXPOSE 5000

# Healthcheck — verify the app responds
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/')" || exit 1

# Run with gunicorn (production WSGI server)
# The app uses create_app() factory from app/__init__.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "120", "--access-logfile", "-", "--error-logfile", "-", "app:create_app()"]
