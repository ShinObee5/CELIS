from app import app
from flask import request,redirect,url_for,render_template,flash
from app import forms


@app.route('/')
@app.route('/index')
def index():
    return render_template('celis.html',title='Home')

@app.route('/basetemplate')
def base():
    return render_template('celis.html',title='template')


@app.route('/register',methods=['POST','GET'])
def sigin():
    form=forms.LoginForm()
    return render_template('signuppage.html',form=form)
