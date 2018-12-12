from app import app
from app.models import User, Post, Player


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Player': Player}
