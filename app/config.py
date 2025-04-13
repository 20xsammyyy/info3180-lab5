import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = os.environ.get('FLASK_DEBUG', 'True') == 'True'  # Ensure it's a boolean value
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')

    # Ensure DATABASE_URL is correctly handled
    DATABASE_URL = os.environ.get('DATABASE_URL', '')
    if DATABASE_URL:
        SQLALCHEMY_DATABASE_URI = DATABASE_URL.replace('postgres://', 'postgresql://')
    else:
        SQLALCHEMY_DATABASE_URI = ''

    SQLALCHEMY_TRACK_MODIFICATIONS = False
