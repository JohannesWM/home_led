from flask import Flask
from config import Config



app = Flask(__name__)
app.config.from_object(Config)
app.config['PERMANENT_SESSION_LIFETIME'] = 1800

from app import routes
