#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random, string


class Config:
    CSRF_ENABLED = True
    SECRET = "livro_flask_de_A_a_Z"
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER = os.path.join(ROOT_DIR, "templates")
    APP = None
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:root@localhost:3306/teste'
    # User: usuario do banco de dados
    # Passwd - senha do usuario
    # Host - ip do banco de dados
    # Porta - Porta do banco de dados
    # database: Nome do banco de dados



class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'  # Endereço do servidor na nuvem
    PORT_HOST = 5000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
    IP_HOST = 'localhost'  # servidor na nuvem
    PORT_HOST = 8080
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'


app_config = {
        'development': DevelopmentConfig(),
        'testing': TestingConfig(),
        'production': ProductionConfig()
        }


#app_active = os.getenv('FLASK_ENV')
app_active = "development"

