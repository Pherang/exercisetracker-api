from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import Config
import logging
from logging.handlers import RotatingFileHandler
import os

webapp = Flask(__name__)
webapp.config.from_object(Config)
db = SQLAlchemy(webapp)
bootstrap = Bootstrap(webapp)

if not webapp.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/exapi.log', maxBytes=10240,
                                         backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    webapp.logger.addHandler(file_handler)

    webapp.logger.setLevel(logging.INFO)
    webapp.logger.info('ExerciseTracker API startup')

from app.api import routes
