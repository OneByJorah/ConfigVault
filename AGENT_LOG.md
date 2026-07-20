# AGENT_LOG.md — ConfigVault Polish Pass

**Repo:** OneByJorah/ConfigVault
**Stack:** Python 3.11, Flask 3.1, Flask-SQLAlchemy, Flask-Migrate, Flask-CORS, PyYAML, paramiko. SQLite (default). Port 5000 (Docker 5001->5000).
**Author credit:** Jhonattan L. Jimenez (@OneByJorah), JorahOne LLC
**Agent:** release-engineering polish pipeline

## Phase 0 — Intake
- Cloned repo. It is a Flask NOC dashboard/API for network config backup.
- Real code present: app factory, models (Device/Backup/Commit/DeviceCommit/Alert), API blueprints (devices/backup/restore/compare/alerts/sync/api).
- Frontend templates exist (index/devices/backup/restore/compare/alerts/cloud) but NO routes serve them — only `/` returns JSON.
- LICENSE is MIT but body still says "JorahOne LLC" placeholder? will verify.

## Bugs found (Phase 1 will confirm by running)
- `app/routes/backup.py:35` `db.func.now().strftime(...)` — SQL expression has no `.strftime`; crashes on backup trigger.
- `app/routes/restore.py:29` `device.config_path = ...` — Device model has no `config_path` column; AttributeError.
- No web UI routes: templates unreachable. README claims `/inventory`,`/backup`, etc.
- `app/__init__.py` loads YAML but only uses SERVER_NAME/SECRET_KEY/DATABASE_URL; fine.
- config/default.conf commits placeholder secrets (FTP_PASS, SECRET_KEY, OXIDIZED_API_KEY) — these are placeholders, not real leaks; move to .env.example.

## Plan
1. venv + install deps, run app, confirm bugs.
2. Fix runtime crashes; add web UI routes so dashboard renders (honest, real).
3. Create .env.example; gitignore .env (already).
4. Dockerfile multi-stage non-root + HEALTHCHECK.
5. Real screenshots via Playwright.
6. Rewrite README honest.
7. gh repo metadata.
8. Commit+push agent/polish-pass.

## Phase 1 — Running locally
- venv + pip install -r requirements.txt: OK (added pytest).
- App boots; DB (SQLite) creates tables.
- Confirmed crashes via test client:
  - `/api/v1/backup` POST → 500 (db.func.now().strftime). FIXED: use datetime.now().
  - `/api/v1/restore` POST → 500 (device.config_path no such column). FIXED: removed line.
  - All web pages returned 404 (templates not found) — app factory rooted at app/ package. FIXED: explicit template_folder/static_folder to repo root.
  - Pages referenced url_for('dashboard') etc → BuildError. FIXED: web blueprint endpoints.
  - SERVER_NAME from config caused 308 redirect on every request. FIXED: dropped SERVER_NAME, env-driven SECRET_KEY/DATABASE_URL.
  - strict_slashes caused 308 on API POSTs without trailing slash. FIXED: app.url_map.strict_slashes=False.
- Added `app/routes/web.py` serving dashboard/devices/backup/restore/compare/alerts/cloud with LIVE DB data.
- Wired templates (index/devices/backup/restore/alerts/compare) to render real data instead of hardcoded demo rows.
- Added `app/seed.py` + `flask seed` command for demo data.
- Added `tests/test_app.py` smoke suite (5 passing).

## Phase 2 — Harden
- Fixed LICENSE copyright to "Jhonattan L. Jimenez / JorahOne LLC".
- Added .env.example (never commit .env).
- .gitignore: added instance/, .env.
- config/default.conf still contains placeholder secrets (demo only, not real). Flagged, not real leaks.
- app.py debug now env-controlled; Dockerfile runs non-root, FLASK_DEBUG=0.

## Phase 3 — Dockerize
- Rewrote Dockerfile: python:3.11-slim, non-root user (uid 10001), HEALTHCHECK on /api/v1/health, EXPOSE 5000.
- docker build OK; docker run serves /api/v1/health 200 and all pages 200.
- docker-compose.yml maps 5001:5000 (unchanged, valid).

## Phase 4 — Screenshots
- Ran app on port 5055 (5000/5005 occupied by other services), seeded demo data.
- Playwright headless chromium captured 4 real screenshots to docs/screenshots/:
  main-dashboard.png, devices.png, backup.png, alerts.png (all ~80-100KB, real content).

## Phase 5 — README
- Rewrote README.md with honest structure, real feature bullets, Docker + manual quick start,
  4 screenshots, architecture, config table, testing, roadmap, author section.

## Phase 6 — Repo metadata
- gh repo edit description + topics (pending).
