#working with flask sqlachemy and flask migrate

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./seconddb.db'
    app.config['SECRET_KEY'] = 'password'

    db.init_app(app)



    login_manager = LoginManager()
    login_manager.init_app(app)

    #how the login manager will load a user
    from models_auth import User

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    #To change the diffault message when your login required in an endpoint
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for('index'))

    bycrypt = Bcrypt(app)
    


    from routes import register_route
    register_route(app, db, bycrypt)
    
    migrate = Migrate(app, db)

    return app
