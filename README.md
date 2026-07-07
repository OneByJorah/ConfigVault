<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/SQLAlchemy-FF6C37?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/rclone-00A6A6?style=for-the-badge&logo=googlecloud&logoColor=white">
</div>

<br>

<div align="center">
  <h1>🛡️ NetVault</h1>
  <p><strong>Network Backup & Asset Management Dashboard</strong></p>
  <p>Centralized device inventory, backup scheduling, snapshot comparison, and alert tracking</p>
  <p>
    <a href="#-features">Features</a> •
    <a href="#-quick-start">Quick Start</a> •
    <a href="#-architecture">Architecture</a> •
    <a href="#-api">API</a>
  </p>
</div>

---

## 📸 Screenshot

![NetVault Dashboard](docs/dashboard.png)
*Network backup and asset management dashboard with device inventory, backup scheduling, and snapshot comparison*

## ✨ Features

- **Device Inventory** — Centralized network device management
- **Backup Scheduling** — Automated backup jobs and logging
- **Snapshot Comparison** — Diff between backup snapshots
- **Data Restoration** — Recovery workflows for network devices
- **Alert Tracking** — Monitor backup failures and issues
- **Cloud Sync** — rclone integration for remote storage
- **SSH Integration** — Paramiko for secure device connections

## 🚀 Quick Start

```bash
git clone https://github.com/OneByJorah/NetVault.git
cd NetVault
pip install -r requirements.txt
python3 setup.py install
# Or run directly
python3 app.py
```

## 🏗️ Architecture

```
NetVault/
├── app/                       # Flask application
│   ├── __init__.py            # App factory
│   ├── config.py              # Configuration
│   ├── models.py              # SQLAlchemy models
│   └── routes/                # Route blueprints
├── static/                    # Static assets (CSS, JS)
├── templates/                 # Jinja2 templates
├── config/                    # Configuration files
├── docs/                      # Documentation
└── requirements.txt           # Dependencies
```

## 🔧 Key Routes

| Endpoint | Description |
|----------|-------------|
| `/inventory` | Device inventory management |
| `/backup` | Backup scheduling & logs |
| `/snapshots` | Snapshot comparison & diff |
| `/restore` | Data restoration workflows |
| `/alerts` | Alert tracking & monitoring |
| `/sync` | Remote synchronization |

## 📄 License

MIT © Jhonattan L. Jimenez

---

<div align="center">
  <p>🛡️ Your network backups, centralized</p>
  <p><a href="https://github.com/OneByJorah">@OneByJorah</a></p>
</div>
