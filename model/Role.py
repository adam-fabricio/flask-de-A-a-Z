# -*- coding: utf-8 -*-
from extensions import db
from sqlalchemy.orm import relationship

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)

    #users = relationship("User", back_populates="funcao")
    def __repr__(self):
        return self.name
