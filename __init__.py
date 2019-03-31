import os
from flask import Flask
from config import Config, DevelopmentConfig
from models import db

app = Flask(__name__)

if os.environ.get('FLASK_ENV', None) == 'production':
    config = Config()
    secret_key = os.environ.get('AIRPORT_APP_SECRET_KEY', None)
else:
    config = DevelopmentConfig()
    secret_key = b'gnjhsudihdf38478GYUG52#W#WD^F^'

app.config.from_object(config)
app.secret_key = secret_key

db.init_app(app)
