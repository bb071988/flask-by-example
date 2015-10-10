from flask import Flask
import os
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Result




@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
        return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()  # uncomment this to run heroku
    print "{}".format(os.environ['APP_SETTINGS'])
    if os.environ['APP_SETTINGS'] == "config.DevelopmentConfig":
        port = int(os.environ.get('PORT', 8080))  # comment these to run heroku
        app.run(host='0.0.0.0', port=port)  
    
