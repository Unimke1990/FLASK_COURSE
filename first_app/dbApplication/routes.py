from flask import render_template, request, flash

from models import Person

def register_route(app, db):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            people = Person.query.all()
            return render_template('index.html', people=people)
        
        elif request.method == 'POST':
            name = request.form.get('name')
            age = int(request.form.get('age'))
            job = request.form.get('job')

            person = Person(name=name, age=age, job=job)

            db.session.add(person)
            db.session.commit()

            people = Person.query.all()
            return render_template('index.html', people=people)

#delete a user
    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()

        db.session.commit()

        people = Person.query.all()
        return render_template('index.html', people=people)


#view  the detail information of a user
    @app.route('/details/<pid>', methods=['GET'])
    def details(pid):
        person = Person.query.filter(Person.pid==pid).first()
        return render_template('details.html', person=person)