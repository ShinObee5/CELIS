from app import app
from flask import request,redirect,url_for,render_template,flash



# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html',title='Home')

@app.route('/basetemplate')
def base():
    return render_template('template.html',title='template')
