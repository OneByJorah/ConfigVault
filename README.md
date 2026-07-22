<div align="center">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/Paramiko-FF6600?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
</div>

<br>

<div align="center">
  <h1>ConfigVault</h1>
  <p><strong>Network Backup & Asset Management Dashboard</strong></p>
  <p>Centralized device inventory, backup scheduling, snapshot comparison, and alert tracking.</p>
  <p>
    <a href="#features">Features</a> •
    <a href="#quick-start">Quick Start</a> •
    <a href="#architecture">Architecture</a> •
    <a href="#contributing">Contributing</a>
  </p>
</div>

---

## Screenshot

![ConfigVault Dashboard](docs/screenshot.png)
*Network backup and asset management dashboard with device inventory and alert tracking.*

## Features

- **Device Inventory** — Centralized network device management and tracking.
- **Backup Scheduling** — Automated backup jobs with logging and history.
- **Snapshot Comparison** — Diff between backup snapshots to detect changes.
- **Data Restoration** — Recovery workflows for network device configurations.
- **Alert Tracking** — Monitor backup failures and system issues.
- **Cloud Sync** — rclone integration for remote backup storage.
- **SSH Integration** — Paramiko for secure device connections.
- **Flask Dashboard** — Professional web interface with SQLAlchemy ORM.

## Quick Start

```bash
git clone https://github.com/OneByJorah/ConfigVault.git
cd ConfigVault

pip install -r requirements.txt
python3 setup.py install

# Run the dashboard
python3 app.py
```

Open **http://localhost:5000** in your browser.

### Docker Deployment

```bash
docker compose up -d
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_APP` | `app.py` | Flask application entry point |
| `DATABASE_URL` | `sqlite:///configvault.db` | Database connection string |
| `RCLONE_REMOTE` | — | rclone remote name for cloud sync |
| `SSH_KEY_PATH` | `~/.ssh/id_rsa` | SSH key for device connections |
| `BACKUP_RETENTION_DAYS` | `30` | Days to keep backup snapshots |
| `ALERT_EMAIL` | — | Email for critical alert notifications |

## Architecture

```
Browser ──HTTP──▶ Flask App ──▶ SQLAlchemy ──▶ SQLite/PostgreSQL
                          │
                          ├──▶ Paramiko (SSH) ──▶ Network Devices
                          ├──▶ rclone ──▶ Cloud Storage
                          └──▶ Alert Engine ──▶ Email/Logs
```

## Tech Stack

- **Backend**: Flask (Python 3.10+), SQLAlchemy
- **Database**: SQLite (default), PostgreSQL (production)
- **SSH**: Paramiko for secure device connections
- **Storage**: rclone for cloud backup sync
- **Deployment**: Docker Compose, systemd

## Project Structure

```
ConfigVault/
├── app/
│   ├── __init__.py          # Flask application factory
│   ├── routes/
│   │   ├── devices.py       # Device management endpoints
│   │   ├── backup.py        # Backup scheduling and execution
│   │   ├── restore.py       # Configuration restoration
│   │   ├── compare.py       # Snapshot comparison
│   │   ├── alerts.py        # Alert tracking and notifications
│   │   └── sync.py          # Cloud sync operations
│   ├── models.py            # SQLAlchemy database models
│   └── config.py            # Application configuration
├── templates/               # Jinja2 HTML templates
├── static/                  # CSS, JS, images
├── setup.py                 # Installation script
├── docker-compose.yml       # Docker deployment
└── .env.example             # Configuration template
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/devices` | GET | List all managed devices |
| `/devices/add` | POST | Add a new device |
| `/backup/schedule` | POST | Schedule backup jobs |
| `/backup/history` | GET | View backup history |
| `/compare/<id1>/<id2>` | GET | Compare two snapshots |
| `/restore/<snapshot_id>` | POST | Restore device configuration |
| `/alerts` | GET | View active alerts |
| `/sync/push` | POST | Push backups to cloud |

## Contributing

Contributions are welcome. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community standards.

## Security

For security concerns, see [SECURITY.md](SECURITY.md). Please report vulnerabilities to **info@jorahone.com** — do not use public issues.

## License

MIT © Jhonattan L. Jimenez

---

<div align="center">
  <p>Network config backup and asset tracking.</p>
  <p><a href="https://github.com/OneByJorah">@OneByJorah</a></p>
</div>
