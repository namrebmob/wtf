# gunicorn.config.py

import fileutils
from environs import Env

env = Env()
env.read_env()

BIND = env.str('GUNICORN_BIND', default='0.0.0.0:80')
WORKER_CLASS = env.str('GUNICORN_WORKER_CLASS', default='sync')
WORKER_TMP_DIR = env.str('GUNICORN_WORKER_TMP_DIR', default=None)
TIMEOUT = env.int('GUNICORN_TIMEOUT', default=30)


def before_fork(server, worker):
    fileutils.touch('/tmp/app-initialized').close()
