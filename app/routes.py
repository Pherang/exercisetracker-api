import json
from datetime import datetime
from flask import Flask, render_template, request
from app.models import User, Exercise
from app.api.errors import bad_request

from app import webapp, db

@webapp.route('/', methods=['GET'])
@webapp.route('/index', methods=['GET'])
def index():
    return render_template('base.html')

@webapp.route('/api/v1/users', methods=['POST'])
def create_user():
    reqbody = request.get_json() or {}
    if 'username' not in reqbody:
        return bad_request("Username required")
    if User.query.filter_by(username=reqbody['username']).first():
        return bad_request("Username already exists")
    user = User(username=reqbody['username'])
    db.session.add(user)
    db.session.commit()
    return jsonify(User.query.filter_by(username=user.username).first())

@webapp.route('/api/v1/exercise', methods=['POST'])
def add_exercise():
    pass

@webapp.route('/api/v1/exercises', methods=['GET'])
def get_exercises():
    testing = request.args
    time = str(datetime.utcnow())
    exerciselog = { 'placeholder-description': 'Pushups',
                    'placeholder-duration': 60,
                    'placeholder-date': time,
                  }
    # return json.dumps( exerciselog)
    return json.dumps(testing)
