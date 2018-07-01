from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    exercises = db.relationship('Exercise', backref='user', lazy=True)
    def __repr__(self):
       return '<User {}>'.format(self.username) 

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(140), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Exercise {}, {}, {}, {}>'.format(self.description,
                                                  self.duration, self.date, self.user)
