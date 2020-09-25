from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app=Flask(__name__)
app.config.from_object(config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)
login=LoginManager(app)

from app import routes,models
