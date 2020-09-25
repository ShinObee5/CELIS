from app import app
from flask import request,redirect,url_for,render_template,flash,get_flashed_messages,flash
from app import forms
from flask_login import current_user,login_user
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('celis.html',title='Home')

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or Password')
            return redirect(url_for('login'))
        login_user(user,remember_me=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html',title='SignIn',form=form)



@app.route('/basetemplate')
def base():
    return render_template('celis.html',title='template')


@app.route('/register',methods=['POST','GET'])
def sigin():
    form=forms.LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        print(form.username.data)
        print(form.password.data)
        print(form.user_role.data)
        print(form.Region.data)
        return redirect('/')
    return render_template('signuppage.html',form=form)
