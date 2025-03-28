# -*- coding: utf-8 -*-
from extensions import db
from model.Role import Role
from passlib.hash import pbkdf2_sha256
from sqlalchemy.orm import relationship


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80),  nullable=False)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    last_update = db.Column(db.DateTime(6), onupdate=db.func.current_timestamp(), nullable=True)
    recovery_code = db.Column(db.String(200), nullable=True)
    active = db.Column(db.Boolean(), default=1, nullable=True)
    role = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    
    funcao = db.relationship("Role", backref="users")




    def get_user_by_email(self):
        """ To Do: implement """
        return ''


    def get_user_by_id(self):
        """ ToDo: implement """
        return ''


    def update (self, obj):
        """ ToDo implement """
        return ''


    def hash_password(self, password):
        try:
            return pbkdf2_sha256.hash(password)
        except Exception as e:
            print(f"Erro ao criptografar senha {e}")


    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)


    def verify_password(self, password_no_hash, password_database):
        try:
            return pbkdf2_sha256.verify(password_no_hash, password_database)
        except ValueError:
            return False

