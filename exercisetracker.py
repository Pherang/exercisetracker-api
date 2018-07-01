from app.models import User, Exercise
from app import webapp, db

@webapp.shell_context_processor
def make_shell_context():
    return {'db':db, 'User': User, 'Exercise': Exercise}
