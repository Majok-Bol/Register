from flask import Flask,render_template
#initialize app with flask
app=Flask(__name__)
@app.route('/')
@app.route('/home',methods=['POST','GET'])
def home():
    message='Welcome to Home page'
    return render_template('home.html',message=message)


@app.route('/register',methods=['POST','GET'])
def register():
    msg='Welcome to Register page'
    return render_template('register.html',msg=msg)
#run app
if __name__=='__main__':
    app.run(debug=True)