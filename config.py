import os
import random, string

class Config:
    CSRF_ENABLED = True
    SECRET = 'flaks_a_z'
    ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
    TEMPLATES_DIR = os.path.join(ROOT_DIR, 'templates')
    APP = None

class DevelopmentConfig(Config):
    Testing = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'

class testingConfig(Config):
    Testing = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 5000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'

class ProductionConfig(Config):
    Testing = False
    DEBUG = False
    IP_HOST = 'localhost'
    PORT_HOST = 8080
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'

app_config = {
    'development': DevelopmentConfig(),
    'testing': testingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FlASK_ENV', 'development')
