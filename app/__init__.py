from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

webapp = Flask(__name__)
webapp.config.from_object(Config)
db = SQLAlchemy(webapp)

from app.api import routes
