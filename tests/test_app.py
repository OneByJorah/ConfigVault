import os
import tempfile

import pytest

os.environ.setdefault("SECRET_KEY", "test-secret-key")


@pytest.fixture
def client():
    from app import create_app, db

    tmp = tempfile.mkdtemp()
    app = create_app()
    app.config["SERVER_NAME"] = None
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(tmp, "test.db")
    app.config["TESTING"] = True
    with app.app_context():
        db.create_all()
    with app.test_client() as c:
        yield c


def auth():
    return {"Authorization": "Bearer test-secret-key"}


def test_health(client):
    assert client.get("/api/v1/health").status_code == 200


def test_web_pages_render(client):
    for page in ["/", "/devices", "/backup", "/restore", "/compare", "/alerts", "/cloud"]:
        assert client.get(page).status_code == 200


def test_devices_unauthorized(client):
    assert client.get("/api/v1/devices").status_code == 401


def test_backup_creates_record(client):
    from app import db
    from app.models import Device

    with client.application.app_context():
        db.session.add(Device(name="rtr1"))
        db.session.commit()
    r = client.post("/api/v1/backup", json={"device": "rtr1", "mode": "full"}, headers=auth())
    assert r.status_code == 201
    assert "version" in r.get_json()


def test_compare_requires_token(client):
    assert client.post("/api/v1/compare", json={}).status_code == 401
