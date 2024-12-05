#session & cookies management, and message flashing

from flask import Flask, render_template, session, make_response, request

app5 = Flask(__name__, template_folder='templates')
app5.secret_key = 'given'


@app5.route('/')
def page5():
    return render_template('page5.html', message='Index')

@app5.route('/set_data')
def set_data():
    session['name'] = 'given'
    session['other'] = 'hello given'
    
    return render_template('page5.html', message='session data set')


@app5.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session ['other']
        return render_template('page5.html', message=f"name: {name}, other: {other}")
    else:
        return render_template('page5.html', message=f"session not found")
    
    
@app5.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('page5.html', message=f"session cleared")

#creating cookies which are saved on the browsers
@app5.route('/create_cookie')
def create_cookie():
    response = make_response(render_template('page5.html', message='cookie set'))
    response.set_cookie(key='cookie_name', value='cookie_value')
    return response


#get cookie information
@app5.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies.get('cookie_name')
    return render_template('page5.html', message=f"cookie value: {cookie_value}")


# Remove cookie
@app5.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('page5.html', message='cookie removed'))
    response.set_cookie('cookie_name', expires=0)
    return response






if __name__ == '__main__':
    app5.run(host='127.0.0.1', port=5502, debug=True)