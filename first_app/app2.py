# learning how to render html contents, redirection, filters, geting dynamic urls of other endpoints, etc

from flask import Flask, request, render_template, redirect, url_for

app2 = Flask(__name__, template_folder='templates')


@app2.route('/')
def hello():
    myname = 'The Awesome Guy'
    myage = '34 year younger'
    mylist = [10, 15, 81, 80, 17, 37]
    return render_template('index.html', myname=myname, myage=myage, mylist=mylist)


@app2.route('/other')
def page2():
    myname = 'given agim'
    return render_template('page2.html', myname=myname)


@app2.route('/redirected')
def redirected():
    return "I am redirected"


#redirect to another endpoint
@app2.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('redirected'))

#redirect to an external url
@app2.route('/redirect_externalURL')
def redirect_external():
    return redirect('https://nipost.gov.ng/')


#create a custom filter
@app2.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]




if __name__ == '__main__':
    app2.run(host='0.0.0.0', port=5555, debug=True)