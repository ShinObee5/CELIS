from app import app
from flask import request,redirect,url_for,render_template,flash,get_flashed_messages,flash
from app import forms
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User,thread,post
from app.forms import LoginForm,RegisterForm
from werkzeug.urls import url_parse
from app import db
from wtforms.validators import ValidationError
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

@app.route('/forum')
@login_required
def forum():
    threads=thread.query.all()
    return render_template('forumhome.html',title='Forum',threads=threads)

@app.route('/thread/<int:thread_id>',methods=['POST','GET'])
@login_required
def forum_(thread_id):
        posts=post.query.filter_by(thread_id=thread_id).order_by(post.time.asc())
        if(request.method=='POST'):
            print(request.form.get('message'))
            if len(request.form.get('message'))==0 :
                flash('Please Type Something',category="danger")
            else:
                BelongsTo=thread.query.filter_by(id=thread_id).first()
                Author=User.query.filter_by(id=current_user.id).first()
                p=post(message=request.form.get('message'),user_id=current_user.id,thread_id=thread_id,BelongsTo=BelongsTo,Author=Author)
                print(p)
                db.session.add(p)
                db.session.commit()
            posts=post.query.filter_by(thread_id=thread_id).order_by(post.time.asc())
            return redirect(url_for('forum_',title='Forum',posts=posts,thread_id=thread_id))
        return render_template('forum.html',title='Forum',posts=posts)

@app.route('/contact')
@login_required
def contactus():
    return render_template('contactus.html',title='Contact Us')

@app.route('/thread/<int:thread_id>/delete_post/<int:post_id>')
@login_required
def delete_post(post_id,thread_id):
    p=post.query.filter_by(id=post_id).first()
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for('forum_',thread_id=thread_id))
