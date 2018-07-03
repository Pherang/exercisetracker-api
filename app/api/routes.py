import json
from datetime import date, datetime
from flask import Flask, render_template, request, jsonify
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
    result = User.query.filter_by(username=user.username).first()
    response = jsonify(result.to_dict())
    response.status_code = 201
    return response

@webapp.route('/api/v1/exercises', methods=['POST'])
def add_exercise():
    reqbody = request.get_json() or {}
    if ('user_id' not in reqbody or 
            'description' not in reqbody or 
            'duration' not in reqbody or 
            'date' not in reqbody):
        return bad_request("Exercise must include user_id, description, duration, and date fields")
    
    # parse the date sent by the client
    try:
        datefield = reqbody['date']
        dateparts = datefield.split('-')
        d = date(int(dateparts[0]),int(dateparts[1]),int(dateparts[2]))
    except:
        return bad_request("Date field not formatted correctly")
    reqbody['date'] = d
    
    exercise = Exercise()
    exercise.from_dict(reqbody)
    db.session.add(exercise)
    db.session.commit()
    result = Exercise.query.filter_by(user_id=exercise.user_id).first()
    response = jsonify(result.to_dict())
    response.status_code = 201
    return response

@webapp.route('/api/v1/exercises', methods=['GET'])
def get_exercises():
    userid = request.args.get('userid', None, type=int)
    if userid is None:
        return bad_request("userid must be included in request")

    exerciselog = Exercise.query.filter_by(user_id=userid).all()
    return json.dumps(exerciselog, indent=4)
