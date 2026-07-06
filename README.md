<!-- j1-brand:v2 -->
<div align="center">

# NetVault

A self-hosted network backup and asset management dashboard — automated backups, snapshot comparison, device inventory, and cloud sync via rclone.

[![GitHub](https://img.shields.io/badge/github-OneByJorah%2FNetVault-FFB300?style=for-the-badge&labelColor=0d0d0c)](https://github.com/OneByJorah/NetVault)
[![License](https://img.shields.io/badge/license-MIT-FFB300?style=for-the-badge&labelColor=0d0d0c)](LICENSE)
[![Language](https://img.shields.io/badge/Python-FFB300?style=for-the-badge&labelColor=0d0d0c)](https://python.org)
[![Built by](https://img.shields.io/badge/built%20by-JorahOne%20LLC-FFB300?style=for-the-badge&labelColor=0d0d0c)](https://github.com/OneByJorah)

</div>

---

## Why This Exists

Network device configs change constantly — and when something breaks, you need to know what changed and how to roll back. NetVault automates config backups across your fleet, stores snapshot history, shows diffs between versions, and syncs to cloud storage via rclone — all from a Flask dashboard.

## Key Features

| Feature | Why It Matters |
|---|---|
| Automated backup scheduling | Set it and forget it — no manual config dumps |
| Snapshot comparison | See exactly what changed between backup versions |
| Device inventory | Central registry of all backed-up network devices |
| One-click restore | Push a known-good config back to the device |
| rclone cloud sync | Offsite backups to S3, B2, Google Drive, or any rclone target |
| Alert tracking | Get notified when backups fail or configs drift |

## Quick Start

```bash
git clone https://github.com/OneByJorah/NetVault.git
cd NetVault
pip install -r requirements.txt
cp .env.example .env   # configure database, rclone, etc.
python3 app.py
```

## Architecture

```
┌──────────┐     ┌──────────────┐     ┌──────────────┐
│  Devices  │────▶│  NetVault     │────▶│  SQLite /     │
│  (SSH)    │     │  Flask App    │     │  PostgreSQL   │
└──────────┘     └──────┬───────┘     └──────────────┘
                         │
                  ┌──────▼───────┐
                  │  rclone       │
                  │  Cloud Sync   │
                  └──────────────┘
```

## Documentation

| Doc | Description |
|---|---|
| [Setup Guide](docs/setup.md) | Installation and configuration |
| [Device Configuration](docs/devices.md) | Adding and managing network devices |
| [Restore Procedures](docs/restore.md) | Rolling back config changes |

---

## License

MIT © JorahOne, LLC — see [LICENSE](LICENSE)

<sub>Part of the JorahOne infrastructure ecosystem.</sub>
