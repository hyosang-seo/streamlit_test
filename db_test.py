import pyrebase
from config import config

firebase = pyrebase.initialize_app(config)
database = firebase.database()