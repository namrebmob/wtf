# gunicorn.config.py

from environs import Env

env = Env()
env.read_env()

# BIND = env.list('GUNICORN_BIND', default=['127.0.0.1:8000'])
WORKER_CLASS = env.str('GUNICORN_WORKER_CLASS', default='sync')
WORKER_TMP_DIR = env.str('GUNICORN_WORKER_TMP_DIR', default=None)
TIMEOUT = env.init('GUNICORN_TIMEOUT', default=30)
