from datetime import datetime
import unittest
from app import webapp, db
from app.models import User, Exercise
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class TestUserModel(unittest.TestCase):

    def setUp(self):
        webapp.config.from_object(TestConfig)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
       
    def test_create_user(self):
        user = User(username='jojo')
        db.session.add(user)
        db.session.commit()
        finduser = User.query.filter_by(username='jojo').first()
        self.assertEqual(user, finduser)

    def test_compare_user(self):
        user1 = User(username='jojo')
        user2 = User(username='rockman')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        finduser = User.query.filter_by(username='rockman').first()
        self.assertNotEqual(user1, finduser)

class TestExerciseModel(unittest.TestCase):

    def setUp(self):
        webapp.config.from_object(TestConfig)
        db.create_all()
        # We need a user to add Exercises to
        u1 = User(username='jojo')

    def tearDown(self):
        db.session.remove()
        db.drop_all()
       
    def test_create_exercise(self):
        exercise1 = Exercise(description='Pushups', duration=15, date=datetime.utcnow(), user_id=1) 
        db.session.add(exercise1)
        db.session.commit()
        exerciselog = Exercise.query.filter_by(user_id=1).first()
        self.assertEqual(exercise1, exerciselog)


if __name__ == '__main__':
    unittest.main(verbosity=2)
