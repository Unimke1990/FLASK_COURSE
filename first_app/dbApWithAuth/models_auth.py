#working with flask sqlachemy and flask migrate

from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
    description = db.Column(db.String)


    def __repr__(self):
        return f"person with username {self.username} and role: {self.role}"
    
    def get_id(self):
        return self.uid
    
    


    