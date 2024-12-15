#program that runs the applications
from app import create_app

flaskAp = create_app()


if __name__ == '__main__':
    flaskAp.run(host='127.0.0.1', debug=True)