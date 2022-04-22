# Integrating HTML with FLASK
from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index2.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score > 40:
        res = 'pass'
    else :
         res ='fail'
    #return "The score is_s "   + str(score)
    return render_template('success.html',result=res)


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
## Read posted values Request module helps to read the posted values

@app.route('/submit',methods=['POST','GET'])
def submit():
    avg = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        python = float(request.form['python'])
        java = float(request.form['java'])
        statistics = float(request.form['statistics'])
        #avg = science + maths + python + java + statistics
        #a,b,c,d,e =100,200,30,40,50
        total_marks  = 500
        avg = (science + maths + python + java + statistics) / 4
        #avg = (a+b+c+d+e)/5
        #per = (marks/total_marks)*100


    s = 'success'

    return redirect(url_for(s,score = avg))



if __name__=='__main__':
    app.run(debug=True)