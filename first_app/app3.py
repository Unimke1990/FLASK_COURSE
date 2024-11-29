#working with file, uploading, conversion to csv, downloading from a download page, etc

import pandas as pd
import os
import uuid
from flask import Flask, render_template, request, Response, send_from_directory, jsonify

app3 = Flask(__name__, template_folder=('templates'))


#get form data
@app3.route('/', methods=['GET', 'POST'])
def page3():
    if request.method == 'GET':
        return render_template('page3.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'given' and password == 'password':
            return 'success'
        else:
            return 'failure'
        
#file upload
@app3.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    
    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type in ['application/msword', 'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
        df = pd.read_excel(file)
        return df.to_html()


#convert excel to csv
@app3.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']
    df = pd.read_excel(file)
    
    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=result.csv'
        }
    
    )
    return response

#sending response to a download page instead
@app3.route('/convert_csv2', methods=['POST'])
def convert_csv2():
    file = request.files['file']
    df = pd.read_excel(file)
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads', filename))
    
    return render_template('downloads.html', filename=filename)


#endpoint to make the download
@app3.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads', filename, download_name='result.csv')


#sending a post request for json data using JS
@app3.route('/handle_request', methods=['POST'])
def handle_request():
    greeting = request.json['greeting']
    name = request.json['name']
    
    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}')
        
    return jsonify({'messge': 'successfully written!'})




if __name__ == '__main__':
    app3.run(host='127.0.0.1', port=5550, debug=True)