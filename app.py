from flask import Flask,render_template,url_for,redirect,flash,request
from wtforms import StringField,EmailField,PasswordField,SubmitField
from wtforms.validators import Length,InputRequired,Email,EqualTo
from flask_wtf import FlaskForm,CSRFProtect
from dotenv import load_dotenv
import os

#initialize app with flask
app=Flask(__name__)
load_dotenv('env')
# csrf=CSRFProtect(app)
# csrf()
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
@app.route('/')
@app.route('/home',methods=['POST','GET'])
def home():
    return render_template('home.html')


@app.route('/register',methods=['POST','GET'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        flash('Account created successfully')
        return redirect(url_for('dashboard'))

    return render_template('register.html',form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
class RegisterForm(FlaskForm):
    username=StringField('Username',validators=[InputRequired(),Length(min=4)])
    email=EmailField('Email address',validators=[InputRequired(),Email()])
    password=PasswordField('Password',validators=[InputRequired(),Length(min=8,max=255)])
    confirm_password=PasswordField('Confirm password',validators=[InputRequired(),EqualTo('password',message='Passwords must match')])
    submit=SubmitField('Register')
    #print details for debugging
    def __repr__(self):
        return f"\nUsername:{self.username}\nEmail address: {self.email}"
    
#run app
if __name__=='__main__':
    app.run(debug=True)