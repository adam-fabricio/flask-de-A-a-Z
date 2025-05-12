from flask import Flask # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate # type: ignore
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy()
migrate = Migrate()

def create_app() -> Flask:
    """
    Create a Flask application instance.
    :return: A Flask application instance.
    """
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Load configuration from a file
    with app.app_context():
        from model import Category, Product, Role, User
        
    
    @app.route('/')
    def index():
        return "Hello, World!"
    
    return app