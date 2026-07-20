import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    from flask import Flask
    from flask_cors import CORS

    CORS()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static"),
    )

    # Load config
    config_file = os.path.join(os.path.dirname(__file__), "..", "config", "default.conf")
    if os.path.exists(config_file):
        import yaml
        with open(config_file) as f:
            config = yaml.safe_load(f)
    else:
        config = {
            "SERVER_NAME": "configvault.local",
            "SECRET_KEY": "dev-secret-key",
            "DATABASE_URL": "sqlite:///configvault.db",
            "FTP_ENABLED": True,
            "SFTP_ENABLED": True,
            "TFTP_ENABLED": True,
            "OXIDIZED_ENABLED": True,
            "GIT_ENABLED": True,
            "CLOUD_SYNC": False,
        }

    app.config.update({
        "SECRET_KEY": os.getenv("SECRET_KEY", config.get("SECRET_KEY", "dev-secret-key")),
        "DATABASE_URL": os.getenv("DATABASE_URL", config.get("DATABASE_URL", "sqlite:///configvault.db")),
        "SQLALCHEMY_DATABASE_URI": os.getenv("DATABASE_URL", config.get("DATABASE_URL", "sqlite:///configvault.db")),
    })

    db.init_app(app)
    migrate.init_app(app, db)
    app.url_map.strict_slashes = False

    @app.cli.command("seed")
    def seed_command():
        """Populate the database with demo data for local preview."""
        from app.seed import seed
        print(seed())

    # Import routes
    from app.routes import alerts, api, backup, compare, devices, restore, sync, web
    app.register_blueprint(devices.bp)
    app.register_blueprint(backup.bp)
    app.register_blueprint(restore.bp)
    app.register_blueprint(compare.bp)
    app.register_blueprint(alerts.bp)
    app.register_blueprint(sync.bp)
    app.register_blueprint(api.bp)
    app.register_blueprint(web.bp)

    return app
