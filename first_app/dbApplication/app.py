#working with flask sqlachemy and flask migrate

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./firstdb.db'
    app.config['SECRET_KEY'] = 'password'

    db.init_app(app)

    from routes import register_route
    register_route(app, db)

    migrate = Migrate(app, db)

    return app