from flask import Flask
import os
app = Flask(__name__)



@app.route('/<name>')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()  # uncomment this to run heroku
    def hello_name(name):
        return "Hello {}".format(name)
    # port = int(os.environ.get('PORT', 8080))  # comment these to run heroku
    # app.run(host='0.0.0.0', port=port)  