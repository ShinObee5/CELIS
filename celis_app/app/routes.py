from app import app
from flask import request,redirect,url_for,render_template,flash,get_flashed_messages,flash
from app import forms
from flask_login import current_user,login_user,logout_user
from app.models import User
from app.forms import LoginForm,RegisterForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('celis.html',title='Home')

@app.route('/courses')
def course():
    return render_template('courses.html',title='Courses')



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


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
    return render_template('signinpage.html',title='SignIn',form=form)



@app.route('/basetemplate')
def base():
    return render_template('template.html',title='template')


@app.route('/register',methods=['POST','GET'])
def register():
    form=forms.RegisterForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        print(form.username.data)
        print(form.password.data)
        print(form.user_role.data)
        print(form.Region.data)
        return redirect('/')
    return render_template('signuppage.html',form=form,title='Register')


@app.route('/contact')
def contactus():
    return render_template('contactus.html',title='Contact Us')
