from flask_login import login_user, logout_user, current_user, login_required
from flask import render_template, request, redirect, url_for, flash

from models_auth import User

def register_route(app, db, bycrypt):

    # @app.route('/', methods=['GET', 'POST'])
    # def index():
    #     if current_user.is_authenticated:
    #         return str(current_user.username)
    #     else:
    #         return 'No user logged in'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
        
            #hash the password
            hashed_password = bycrypt.generate_password_hash(password)

            user = User(username=username, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))



    #login a user
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter(User.username == username).first()

            if bycrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash('Wrong login credentilas. Try again')
                return redirect(url_for('login'))

    # @app.route('/login/<uid>')
    # def login(uid):
    #     user = User.query.get(uid)
    #     login_user(user)
    #     return 'Logging successfull'
    

    #logout a user
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))
    
    #setting an endpoint with loging required
    @app.route('/secret')
    @login_required
    def secret():
        users = User.query.all()
        return render_template('secret.html', users=users)