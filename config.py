import os
basedir = os.path.abspath(os.path.dirname(__file__))
port = int(os.environ.get('PORT', 5000))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xa9w\xb9{\xbbC;\x0bQ>\xd8\xfb \x03o\x90'
    SQLALCHEMY_DATABASE_URI = app.config('postgres://nckbhqxhruvwcz:efb53cfe3d5fc544849082317adf699dacde344d42fed6fd5a427ba8f3d2687b@ec2-54-235-193-0.compute-1.amazonaws.com:5432/d8gbnciq0f9fpb') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
