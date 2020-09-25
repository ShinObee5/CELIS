from app import app
from flask import request,redirect,url_for,render_template,flash,get_flashed_messages,flash
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
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        print(form.username.data)
        print(form.password.data)
        print(form.user_role.data)
        print(form.Region.data)
        return redirect('/')
    return render_template('signuppage.html',form=form)
