import os

from flask import Flask
from flask_bootstrap import Bootstrap
# from config import Config


from os.path import join
from dotenv import load_dotenv

print(os.environ.get('APP_SETTINGS'))

# check for environment
if os.environ.get('APP_SETTINGS') is None:
    dotenv_path = join(os.path.abspath(os.path.dirname(__name__)), '.env') # Path to .env file
    load_dotenv(dotenv_path)
else:
    pass

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

bootstrap = Bootstrap(app)
# app.config.from_object(Config)

from app import routes
