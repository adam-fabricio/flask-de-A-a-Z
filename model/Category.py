from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active
from model.User import User

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return self.name
