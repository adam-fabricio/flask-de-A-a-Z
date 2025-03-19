#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from config import app_config, app_active
from extensions import db, migrate
from model.User import User
from model.Role import Role
from model.Category import Category
from model.Product import Product


config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return 'Hello World!'

    return app


