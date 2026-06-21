# NetVault — Network Backup & Asset Management

**Version:** v1.0  
**Status:** Active Development  
**Repository:** https://github.com/OneByJorah/NetVault

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Features](#features)
- [Getting Started](#getting-started)
- [Service Management](#service-management)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Overview

NetVault is a network backup and asset management dashboard. It inventories devices, schedules backups, compares snapshots, restores data, and tracks alerts — all from a local web UI.

Built for IT teams who want a single view into backup health and asset state.

---

## Architecture

Client → Flask web UI → backend routes (`app/routes/`) → SQLAlchemy models (`app/models.py`) → storage backends (`rclone`, `paramiko`, GitHub API).

Routes:
- `/devices` — inventory
- `/backup` — schedules and runs
- `/restore` — restores from snapshots
- `/compare` — diff snapshots
- `/alerts` — alerting and status
- `/sync` — remote sync
- `/api` — JSON API

Secrets are loaded via `config/default.conf`.

---

## Technology Stack

| Layer | Stack |
|---|---|
| Runtime | Linux (Ubuntu 22.04+) |
| Backend | Python / Flask / Flask-SQLAlchemy / Flask-Migrate |
| Frontend | HTML + Jinja templates |
| Networking | paramiko (SSH), rclone, PyGithub |
| Auth | bcrypt |
| VCS | Git + GitHub (`github.com/OneByJorah/NetVault`) |

---

## Features

- **Device inventory**: track hosts and credentials.
- **Backup scheduling**: run and log backup jobs.
- **Compare snapshots**: diff prior and current backup sets.
- **Restore**: recovery workflow from snapshots.
- **Alerts**: alert state for devices and jobs.
- **Cloud sync**: support for remote/sync targets.

---

## Getting Started

```bash
# 1. Clone
git clone https://github.com/OneByJorah/NetVault.git
cd NetVault

# 2. Install
pip install -r requirements.txt

# 3. Configure
cp config/default.conf config/local.conf
# Edit local.conf for your storage and credentials.

# 4. Run
python -m flask run
```

---

## Service Management

```bash
# Run
python -m flask run

# Stop
Ctrl+C
```

---

## Project Structure

```
NetVault/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   └── routes/
│       ├── __init__.py
│       ├── alerts.py
│       ├── api.py
│       ├── backup.py
│       ├── compare.py
│       ├── devices.py
│       ├── restore.py
│       └── sync.py
├── static/
│   └── styles.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── devices.html
│   ├── backup.html
│   ├── restore.html
│   ├── compare.html
│   ├── alerts.html
│   └── cloud.html
├── config/
│   └── default.conf
├── requirements.txt
├── setup.py
└── init-db.sql
```

---

## Screenshots

_(Screenshots will be added after build/run capture.)_

---

## Contributing

1. Create a feature branch off `main`.
2. Keep storage and credential logic in `config/`.
3. Submit a PR with description and screenshots for UI changes.

---

## License

MIT

---

## Author

Built by **Jhonattan L. Jimenez**.
