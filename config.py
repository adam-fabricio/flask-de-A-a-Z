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


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT_HOST)


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'  # Endereço do servidor na nuvem
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT_HOST)


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
    IP_HOST = 'localhost'  # servidor na nuvem
    PORT_HOST = 8080 
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT_HOST)


app_config = {
        'development': DevelopmentConfig(),
        'testing': TestingConfig(),
        'production': ProductionConfig()
        }


app_active = os.getenv('FLASK_ENV')

