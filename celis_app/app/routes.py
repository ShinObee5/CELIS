from app import app
from flask import request,redirect,url_for,render_template,flash,get_flashed_messages,flash
from app import forms
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User
from app.forms import LoginForm,RegisterForm
from werkzeug.urls import url_parse
from app import db

@app.route('/')
@app.route('/index')
def index():
    return render_template('celis.html',title='Home')

@app.route('/courses')
@login_required
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
        user=User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Email or Password',category="danger")
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc!='':
            next_page=url_for('index')
        return redirect(next_page)
    return render_template('signinpage.html',title='SignIn',form=form)



@app.route('/basetemplate')
def base():
    return render_template('template.html',title='template')


@app.route('/register',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=forms.RegisterForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,user_role=form.user_role.data,Region=form.Region.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Successfully Registered',category="success")
        print(form.password.data)
        print(form.user_role.data)
        print(form.Region.data)
        return redirect(url_for('login'))
    return render_template('signuppage.html',form=form,title='Register')


@app.route('/contact')
def contactus():
    return render_template('contactus.html',title='Contact Us')
