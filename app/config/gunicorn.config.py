# gunicorn.config.py

from environs import Env

env = Env()
env.read_env()

WORKER_CLASS = env.str('GUNICORN_WORKER_CLASS', default='sync')
WORKER_TMP_DIR = env.str('GUNICORN_WORKER_TMP_DIR', default=None)
TIMEOUT = env.int('GUNICORN_TIMEOUT', default=30)

def when_ready(server):
    open('/tmp/app-initialized', 'w').close()
