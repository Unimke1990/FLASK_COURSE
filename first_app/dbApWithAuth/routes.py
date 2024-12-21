from flask import render_template, request, flash

from models_auth import User

def register_route(app, db):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            users = User.query.all()
            return render_template('index.html', users=users)
        
        elif request.method == 'POST':
            name = request.form.get('name')
            age = int(request.form.get('age'))
            job = request.form.get('job')

            user = User(name=name, age=age, job=job)

            db.session.add(user)
            db.session.commit()

            user = User.query.all()
            return render_template('index.html', user=user)

#delete a user
    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        User.query.filter(User.pid == pid).delete()

        db.session.commit()

        user = User.query.all()
        return render_template('index.html', user=user)


#view  the detail information of a user
    @app.route('/details/<pid>', methods=['GET'])
    def details(pid):
        user = User.query.filter(User.pid==pid).first()
        return render_template('details.html', user=user)
    