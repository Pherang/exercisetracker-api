from flask import Flask, render_template

from app import webapp

@webapp.route('/', methods=['GET'])
@webapp.route('/index', methods=['GET'])
def index():
    return render_template('base.html')

@webapp.route('/api/v1/exercise/new-user', methods=['POST'])
def create_user():
    pass

@webapp.route('/api/v1/exercise/add', methods=['POST'])
def add_exercise():
    pass

@webapp.route('/api/v1/exercise/log')
def get_exercises():
    pass


