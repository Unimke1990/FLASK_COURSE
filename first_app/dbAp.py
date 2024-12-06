#working with flask sqlachemy and flask migrate

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    dbAp = Flask(__name__, template_folder='templates')
    