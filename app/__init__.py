from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import pusher

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

pusher_client = pusher.Pusher(
    app_id='628052',
    key='2c712e9027d8604455b8',
    secret='a7e5e6f8846b3620a7b0',
    cluster='us2',
    ssl=True)


from app import routes, models
