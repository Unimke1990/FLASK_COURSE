from flask_login import login_user, logout_user, current_user, login_required
from flask import render_template, request

from models_auth import User

def register_route(app, db, bycrypt):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        return ""
    
    #login a user
    @app.route('/login/<uid>')
    def login(uid):
        login_user(uid)
        return 'Logging successfull'