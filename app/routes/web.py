"""HTML dashboard routes for ConfigVault NOC."""

from flask import Blueprint, render_template

from app import db
from app.models import Alert, Backup, Device

bp = Blueprint("web", __name__)


@bp.route("/")
def dashboard():
    devices = Device.query.all()
    backups = Backup.query.order_by(Backup.timestamp.desc()).all()
    alerts = Alert.query.order_by(Alert.timestamp.desc()).all()
    active_alerts = [a for a in alerts if not a.resolved]
    return render_template(
        "index.html",
        devices=devices,
        backups=backups,
        alerts=alerts,
        active_alerts=active_alerts,
        total_devices=len(devices),
        recent_backups=len(backups),
        alert_count=len(active_alerts),
        cloud_sync=0,
    )


@bp.route("/devices")
def devices_page():
    devices = Device.query.all()
    return render_template("devices.html", devices=devices)


@bp.route("/backup")
def backup_page():
    devices = Device.query.all()
    backups = Backup.query.order_by(Backup.timestamp.desc()).all()
    schedules = [
        {"name": "Daily Backup", "interval": "Every 24 hours", "enabled": True},
        {"name": "Weekly Backup", "interval": "Every 7 days", "enabled": True},
        {"name": "Monthly Backup", "interval": "Every 30 days", "enabled": False},
    ]
    return render_template(
        "backup.html", devices=devices, backups=backups, schedules=schedules
    )


@bp.route("/restore")
def restore_page():
    devices = Device.query.all()
    backups = Backup.query.order_by(Backup.timestamp.desc()).all()
    return render_template("restore.html", devices=devices, backups=backups)


@bp.route("/compare")
def compare_page():
    backups = Backup.query.order_by(Backup.timestamp.desc()).all()
    return render_template("compare.html", backups=backups)


@bp.route("/alerts")
def alerts_page():
    alerts = Alert.query.order_by(Alert.timestamp.desc()).all()
    return render_template("alerts.html", alerts=alerts)


@bp.route("/cloud")
def sync_page():
    return render_template("cloud.html")
