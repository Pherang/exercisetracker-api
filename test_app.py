from datetime import datetime
import unittest
from app import webapp, db
from app.models import User, Exercise
from config import Config


class TestConfig(Config):
    pass


class TestUserModel(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
