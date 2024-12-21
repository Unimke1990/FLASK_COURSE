#working with flask sqlachemy and flask migrate

from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)

    def __repr__(self):
        return f"person with name {self.name} and age: {self.age}"
    
    


    