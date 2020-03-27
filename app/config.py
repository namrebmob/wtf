# app/config.py

from environs import Env

env = Env()
env.read_env()

DEBUG = env.bool('FLASK_DEBUG', default=False)
SECRET_KEY = env.str('SECRET_KEY')
CHUNK_SIZE = env.int('CHUNK_SIZE', default=1024)
