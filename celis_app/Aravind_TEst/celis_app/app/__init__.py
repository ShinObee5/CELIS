from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#general configs
app=Flask(__name__)
app.config.from_object(config)
#DB Configs
db=SQLAlchemy(app)
migrate=Migrate(app,db)
#Login Configs
login=LoginManager(app)
login.login_view='login'
login.message='Please Login To Access The Page'
login.login_message_category='info'

from app import routes,models
