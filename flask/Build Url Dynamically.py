## Build URL Dynamically
## Variable Rules and URL building

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello Python!"

@app.route('/success/<int:score>')
def success(score):
    return "The score is_s "   + str(score)

@app.route('/failed/<int:score>')
def fail(score):
    return "The score is_p " + str(score)

@app.route('/result_status/<int:marks>')
def result_(marks):
    result = ""
    if marks >= 50:
        result= 'fail'
    elif marks >=75:
        result= 'success'
    else:
        result = 'fail'
    return redirect(url_for(result,score=marks))

if __name__=='__main__':
    app.run(debug=True)