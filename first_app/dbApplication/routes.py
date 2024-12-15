from flask import render_template, request

from models import Person

def register_route(app, db):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        people = Person.query.all()
        return render_template('index.html', people=people)