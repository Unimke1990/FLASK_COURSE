#introduction to flask, request, and how to create and work with routes

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World<h1/>"


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if (request.method == 'GET'):
        return "You sent a get request\n"
    elif (request.method == 'POST'):
        return "you sent a post request\n"
    else:
        return "Learning Flask from scratch"
    

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}\n param_args: {request.view_args}"


@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


@app.route('/handle_query_params')
def query():
    return request.args.to_dict()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)