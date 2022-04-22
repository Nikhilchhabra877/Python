from flask import  Flask

import  requests
#WSGI
app = Flask(__name__)

@app.route('/') ## Decorator
def welcome():
    return "Welcome to Flask world! please read it carefully"

@app.route('/name') ## Decorator
def welcome1():
    return "Welcome to Flask world! please read it carefully please"


if __name__ == '__main__':
    app.run(debug=True)