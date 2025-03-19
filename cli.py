# -*- coding: utf-8 -*-
from flask.cli import FlaskGroup
from app import create_app
from config import app_active
from extensions import db, migrate

app = create_app(app_active)

cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()
