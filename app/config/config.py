# app/config.py

from environs import Env

env = Env()
env.read_env()

FLASK_ENV = env.str('FLASK_ENV', default='production')
DEBUG = env.bool('FLASK_DEBUG', default=False)
SECRET_KEY = env.str('SECRET_KEY')
MAX_CONTENT_LENGTH = env.int('MAX_CONTENT_LENGTH', default=None)
