"""Entry point for ConfigVault NOC application.

Usage:
    python3 app.py
"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    import os

    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    port = int(os.getenv("CONFIGVAULT_PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=debug)
