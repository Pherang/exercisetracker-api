from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    exercises = db.relationship('Exercise', backref='user', lazy=True)

    def to_dict(self):
        user = {
                'id': self.id,
                'username': self.username,
               }
        return user

    def __repr__(self):
       return '<User {}>'.format(self.username) 

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(140), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def from_dict(self, data):
        for field in ['user_id', 'description', 'duration', 'date']:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        exercise = {
                'id': self.id,
                'description': self.description,
                'duration': self.duration,
                'date': self.date,
                'user_id': self.user_id,
               }
        return exercise

    def to_log_dict(self, collection):
        pass

    def __repr__(self):
        return '<Exercise {}, {}, {}, {}>'.format(self.description,
                                                  self.duration, self.date, self.user)
