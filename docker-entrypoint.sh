#!/bin/bash
# NetVault Docker Entrypoint
# Handles first-run setup and credential onboarding

set -e

# If .env doesn't exist, run setup wizard
if [ ! -f /app/.env ]; then
    echo "============================================"
    echo "  NetVault — First Run Setup"
    echo "============================================"
    echo ""
    echo "No configuration found. Let's set up NetVault."
    echo ""
    
    # Generate random secret
    SECRET=$(python3 -c "import secrets; print(secrets.token_hex(32))")
    
    # Prompt for config
    read -p "Admin username [admin]: " ADMIN_USER
    ADMIN_USER=${ADMIN_USER:-admin}
    
    read -s -p "Admin password (leave blank for random): " ADMIN_PASS
    echo ""
    ADMIN_PASS=${ADMIN_PASS:-$(python3 -c "import secrets; print(secrets.token_urlsafe(16))")}
    
    read -p "Database path [data/netvault.db]: " DB_PATH
    DB_PATH=${DB_PATH:-data/netvault.db}
    
    read -p "Port [5000]: " PORT
    PORT=${PORT:-5000}
    
    # Write .env
    cat > /app/.env <<EOF
SECRET_KEY=${SECRET}
ADMIN_USER=${ADMIN_USER}
ADMIN_PASS=${ADMIN_PASS}
DATABASE_URL=sqlite:///${DB_PATH}
PORT=${PORT}
LOG_LEVEL=INFO
EOF
    
    echo ""
    echo "✅ Configuration saved to /app/.env"
    echo "   Admin user: ${ADMIN_USER}"
    echo "   Admin pass: ${ADMIN_PASS}"
    echo ""
    echo "⚠️  Save these credentials — they won't be shown again."
    echo "============================================"
fi

# Source .env
export $(grep -v '^#' /app/.env | xargs)

# Initialize database
python3 -c "
from app import create_app
app = create_app()
" 2>/dev/null || true

echo "Starting NetVault..."
exec "$@"
