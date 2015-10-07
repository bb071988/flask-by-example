from flask import Flask
import os
app = Flask(__name__)



@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()  # uncomment this to run heroku
    # port = int(os.environ.get('PORT', 8080))  # comment these to run heroku
    # app.run(host='0.0.0.0', port=port)  