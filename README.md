# NetVault

> Linux network configuration backup and FTP server platform.

![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-%23FFB300?style=for-the-badge)
![Language](https://img.shields.io/badge/language-Python-informational?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-linux-informational?style=for-the-badge)

NetVault is an enterprise-grade, ops-precise platform built for VIDE and SMB operations. Run it solo. Deliver results.

- **Device inventory**: track hosts and credentials.
- **Backup scheduling**: run and log backup jobs.
- **Compare snapshots**: diff prior and current backup sets.
- **Restore**: recovery workflow from snapshots.
- **Alerts**: alert state for devices and jobs.
- **Cloud sync**: support for remote/sync targets.

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

| Layer | Stack |
|---|---|
| Runtime | Linux (Ubuntu 22.04+) |
| Backend | Python / Flask / Flask-SQLAlchemy / Flask-Migrate |
| Frontend | HTML + Jinja templates |
| Networking | paramiko (SSH), rclone, PyGithub |
| Auth | bcrypt |
| VCS | Git + GitHub (`github.com/OneByJorah/NetVault`) |

---

## Quickstart

```bash
git clone https://github.com/OneByJorah/NetVault.git
cd NetVault
# Follow in-repo setup instructions
```
Verify by checking service health or running the in-repo test command.

## Roadmap

- Feature parity with production requirements
- Observability and alerting expansions
- Community feedback integration

## License

MIT — Copyright JorahOne, LLC. See [LICENSE](LICENSE) for details.

---

[OneByJorah](https://github.com/OneByJorah) · [JorahOne-Services](https://github.com/JorahOne-Services)
