"""Seed the database with demo devices, backups, and alerts for local preview."""

from datetime import datetime, timedelta

from app import db
from app.models import Alert, Backup, Device


def seed():
    if Device.query.first():
        return "Database already seeded — skipping."

    devices = [
        Device(name="cisco-rtr-1", hostname="cisco-rtr-1", ip_address="192.168.1.1",
               os_type="IOS-XE", protocol="ssh", port=22, enabled=True),
        Device(name="juniper-sw-2", hostname="juniper-sw-2", ip_address="192.168.1.2",
               os_type="JunOS", protocol="ssh", port=22, enabled=True),
        Device(name="arista-swt-3", hostname="arista-swt-3", ip_address="192.168.1.3",
               os_type="EOS", protocol="ssh", port=22, enabled=True),
        Device(name="fortigate-fw-4", hostname="fortigate-fw-4", ip_address="192.168.1.4",
               os_type="FortiOS", protocol="ssh", port=22, enabled=False),
    ]
    db.session.add_all(devices)
    db.session.commit()

    now = datetime.now()
    for i, dev in enumerate(devices):
        ts = now - timedelta(hours=2 + i * 3)
        backup = Backup(
            device_id=dev.id,
            version=f"full-{ts.strftime('%Y%m%d%H%M%S')}",
            timestamp=ts,
            config_file=f"/var/lib/configvault/backup/{dev.name}_running.conf",
            size=40000 + i * 5000,
            checksum=f"sha256:{dev.name}",
            status="completed" if dev.enabled else "failed",
        )
        db.session.add(backup)
        dev.last_backup = ts
        dev.backup_count = 1

    alerts = [
        Alert(device_id=1, type="Config Change", level="critical",
              message="cisco-rtr-1 - Config change detected", timestamp=now - timedelta(hours=2)),
        Alert(device_id=2, type="Backup", level="info",
              message="juniper-sw-2 - Scheduled backup completed", timestamp=now - timedelta(hours=5)),
        Alert(device_id=3, type="Connection", level="warning",
              message="arista-swt-3 - Failed to connect", timestamp=now - timedelta(days=1)),
        Alert(device_id=4, type="Certificate", level="warning",
              message="fortigate-fw-4 - SSL certificate expiring in 30 days",
              timestamp=now - timedelta(days=2)),
    ]
    db.session.add_all(alerts)
    db.session.commit()
    return "Seeded demo data."
