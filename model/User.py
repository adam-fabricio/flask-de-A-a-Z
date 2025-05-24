from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active
from model.Role import Role
from passlib.hash import pbkdf2_sha256
from sqlalchemy.orm import relationship


config = app_config[app_active]
db = SQLAlchemy(config.APP)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    last_update = db.Column(db.DateTime(6), onupdate=db.func.current_timestamp(), nullable=True)
    recovery_code = db.Column(db.String(200), nullable=True)
    active = db.Column(db.Boolean(), default=1, nullable=True)
    role = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False)
    funcao = relationship(Role)

    def get_user_by_email(self):
        """Todo: Implementar método para buscar usuário por email"""
        return ''

    def get_user_by_id(self):
        """Todo: Implementar método para buscar usuário por id"""
        return ''

    def update(self, obj):
        """Todo: Implementar método para atualizar usuário"""
        return ''
    
    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)

    def hash_password(self, password):
        """Hash a password using pbkdf2_sha256 algorithm."""
        self.password = pbkdf2_sha256.hash(password)

    def verify_password(self, password_no_hash, password_database):
        """Verify a password against a hashed password."""
        try:
            return pbkdf2_sha256.verify(password_no_hash, password_database)
        except ValueError:
            # Handle the case where the password is not valid
            return False
    
    def __repr__(self):
        return f'{self.id} - {self.username}'
        