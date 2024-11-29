#working with static files, and integrating Bootstrap

from flask import Flask, render_template, request

app4 = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')


@app4.route('/')
def hello():
    return render_template('page4.html')




if __name__ == '__main__':
    app4.run(host='127.0.0.1', port=5505, debug=True)