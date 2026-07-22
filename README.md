# ConfigVault

Network backup and asset management dashboard — centralized device inventory, backup scheduling, snapshot comparison, and alert tracking.

![status](https://img.shields.io/badge/status-active-FFB300?style=flat-square)
![language](https://img.shields.io/badge/python-3.10+-0d0d0c?style=flat-square)
![license](https://img.shields.io/badge/license-MIT-FFB300?style=flat-square)

## Overview

ConfigVault is a self-hosted network backup and asset management dashboard that provides centralized device inventory, automated backup scheduling, snapshot comparison, data restoration workflows, and alert tracking. It integrates rclone for cloud sync and Paramiko (SSH) for secure device connections. Built with Flask and SQLAlchemy.

## Features

- Device inventory — centralized network device management
- Backup scheduling — automated backup jobs and logging
- Snapshot comparison — diff between backup snapshots
- Data restoration — recovery workflows for network devices
- Alert tracking — monitor backup failures and issues
- Cloud sync — rclone integration for remote storage
- SSH integration — Paramiko for secure device connections
- Flask + SQLAlchemy web dashboard

## Architecture / Tech Stack

- **Backend**: Flask (Python), SQLAlchemy
- **Database**: SQLite / PostgreSQL
- **Storage**: rclone (cloud sync)
- **SSH**: Paramiko
- **Deployment**: Docker Compose, local install

## Installation

```bash
git clone https://github.com/OneByJorah/ConfigVault.git
cd ConfigVault

pip install -r requirements.txt
python3 setup.py install

# Or run directly
python3 app.py

# Or Docker
docker compose up -d
```

## Usage

1. Open the web dashboard
2. Add your network devices
3. Configure backup schedules
4. Monitor alerts and compare snapshots

## License

MIT — see [LICENSE](LICENSE).

---
Part of the JorahOne / J1 ecosystem — network config backup and asset tracking.
