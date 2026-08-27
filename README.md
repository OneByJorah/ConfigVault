<div align="center">

# ConfigVault

**Network Configuration Backup & Asset Management Dashboard**

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1-000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?logo=python&logoColor=white)](https://www.sqlalchemy.org/)
[![Paramiko](https://img.shields.io/badge/Paramiko-5.0-4B8BBE?logo=python&logoColor=white)](https://www.paramiko.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=fff)](docker-compose.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

<p align="center">
  <img src="docs/screenshots/configvault-dashboard.png" alt="ConfigVault Dashboard" width="90%">
</p>

---

## Overview

ConfigVault is a lightweight NOC-style dashboard for managing network-device configuration backups. It gives small teams a simple web UI to inventory routers, switches, firewalls, and APs; schedule backups; compare snapshots; and push history to cloud storage via rclone.

### Why ConfigVault?

| Concern | ConfigVault Approach |
|---------|---------------------|
| **Single-node deploy** | Flask + SQLite runs anywhere |
| **No cloud lock-in** | Self-hosted; optional rclone sync |
| **SSH/SFTP safety** | Paramiko; keys/secrets via env only |
| **No database server** | SQLite default; PostgreSQL ready |

## Features

| Feature | Status | Description |
|---------|--------|-------------|
| Device Inventory | ✅ | Manage routers, switches, firewalls, and APs |
| Backup Scheduling | ✅ | Trigger backups manually or via cron hooks |
| Snapshot Diff | ✅ | Side-by-side config comparison |
| Config Restore | ✅ | Roll back to any historical backup |
| Alert Engine | ✅ | Slack, Teams, Discord, email webhooks |
| Cloud Sync | ⚙️ | rclone integration (bring your own config) |
| SSH Integration | ✅ | Paramiko-based SSH/SFTP to devices |
| NOC Dashboard | ✅ | Dark-theme web UI with live status cards |

## Quick Start

### Local (virtualenv)

```bash
git clone https://github.com/OneByJorah/ConfigVault.git
cd ConfigVault
./install.sh          # creates venv, installs deps, copies .env.example
. ./venv/bin/activate
python app.py         # http://localhost:8103
```

On Windows:

```powershell
python -m venv venv
.\venv\Scripts\pip install -r requirements.txt
.\venv\Scripts\python app.py
```

### Docker Compose

```bash
cp .env.example .env   # edit SECRET_KEY and any optional settings
docker compose up -d   # http://localhost:8103
```

> **Note:** ConfigVault defaults to SQLite with persistent `./instance` and `./configs` directories mounted into the container. For production, switch to PostgreSQL by setting `DATABASE_URL`.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.11, Flask 3, Flask-SQLAlchemy, Flask-Migrate |
| **Frontend** | Jinja2 templates + Bootstrap/custom CSS |
| **SSH/SFTP** | Paramiko |
| **Database** | SQLite (default), PostgreSQL (optional) |
| **Cloud Sync** | rclone (optional) |
| **Container** | Docker / Docker Compose |

## Screenshots

| Dashboard |
|:--:|
| <img src="docs/screenshots/configvault-dashboard.png" alt="ConfigVault Dashboard" width="100%"> |

## Architecture

```
┌─────────────┐     HTTP      ┌──────────────────┐     ┌──────────────┐
│   Browser   │ ──────────▶   │  Flask (NOC UI)  │────▶│  SQLAlchemy  │
│  (Dark UX)  │ ◀──────────── │  Port 8103       │◀────│  SQLite/PG   │
└─────────────┘               └──────────────────┘     └──────────────┘
                                       │
                     ┌─────────────────┼─────────────────┐
                     ▼                 ▼                  ▼
             ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
             │   Paramiko   │  │    rclone    │  │ Alert Engine │
             │   SSH/SFTP   │  │  Cloud Sync  │  │ Slack/Email  │
             └──────┬───────┘  └──────┬───────┘  └──────────────┘
                    │                 │
                    ▼                 ▼
             ┌──────────────┐  ┌──────────────┐
             │   Network    │  │  S3 / GDrive │
             │   Devices    │  │  / B2 / O365 │
             └──────────────┘  └──────────────┘
```

## Project Structure

```
ConfigVault/
├── app/                      # Flask application package
│   ├── __init__.py           # Application factory
│   ├── config.py             # Environment-based configuration
│   ├── models.py             # SQLAlchemy ORM models
│   └── routes/               # API route blueprints
│       ├── devices.py
│       ├── backup.py
│       ├── restore.py
│       ├── compare.py
│       ├── alerts.py
│       ├── sync.py
│       └── api.py
├── templates/                # Jinja2 HTML templates
├── static/                   # Static assets (CSS/JS)
├── config/                   # YAML runtime configuration
├── instance/                 # SQLite database storage (created at runtime)
├── configs/                  # Git-backed config history (created at runtime)
├── docs/                     # Documentation & assets
│   └── screenshots/
├── app.py                    # Entry point
├── requirements.txt          # Python dependencies
├── Dockerfile                # Container image
├── docker-compose.yml        # Compose stack
├── install.sh                # Linux/macOS installer
├── .env.example              # Environment template
└── setup.py                  # Package installer
```

## Configuration

ConfigVault reads environment variables first, then falls back to `config/default.conf`. Create `.env` from `.env.example` and set at least `SECRET_KEY`.

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | `sqlite:///instance/configvault.db` | SQLAlchemy database URI |
| `SERVER_NAME` | `configvault.local` | Server hostname |
| `SECRET_KEY` | `dev-secret-key` | Flask secret key — **change this** |
| `FTP_ENABLED` | `false` | Enable FTP backup target |
| `SFTP_ENABLED` | `false` | Enable SFTP backup target |
| `OXIDIZED_ENABLED` | `false` | Enable Oxidized integration |
| `CLOUD_SYNC` | `false` | Enable rclone cloud sync |
| `SLACK_WEBHOOK` | — | Slack webhook URL |
| `DISCORD_WEBHOOK` | — | Discord webhook URL |
| `TEAMS_WEBHOOK` | — | Microsoft Teams webhook |

> For security, disable unused protocols (`FTP_ENABLED=false`, etc.) and never commit credentials to git.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/health` | `GET` | Health check |
| `/api/v1/config` | `GET` | App configuration |
| `/api/v1/devices` | `GET` | List devices |
| `/api/v1/devices` | `POST` | Add a device |
| `/api/v1/backup` | `POST` | Trigger backup |
| `/api/v1/backup/schedule` | `GET` | List schedules |
| `/api/v1/restore` | `POST` | Restore config |
| `/api/v1/compare` | `POST` | Diff snapshots |
| `/api/v1/alerts` | `GET` | List alerts |
| `/api/v1/sync` | `POST` | Push to cloud |
| `/api/v1/sync/status` | `GET` | Sync status |

## Deployment

### Docker (recommended for self-hosting)

```bash
cp .env.example .env
# edit .env — set SECRET_KEY, disable protocols you don't use
docker compose up -d
docker compose logs -f
```

### Manual

```bash
./install.sh
source venv/bin/activate
python app.py
```

## Upgrading

```bash
git pull
source venv/bin/activate
pip install -r requirements.txt
flask db upgrade
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community standards.

## Security

Found a vulnerability? Please report to **security@example.com** per [SECURITY.md](SECURITY.md) — do not use public issues.

## License

[MIT](LICENSE) © Jhonattan L. Jimenez (OneByJorah)

---

<p align="center">
  <a href="https://github.com/OneByJorah">OneByJorah</a>
  ·
  <a href="https://github.com/OneByJorah/ConfigVault/issues">Issues</a>
  ·
  <a href="CHANGELOG.md">Changelog</a>
</p>
