from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import Config

webapp = Flask(__name__)
webapp.config.from_object(Config)
db = SQLAlchemy(webapp)
bootstrap = Bootstrap(webapp)

from app.api import routes
