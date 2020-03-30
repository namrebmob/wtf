# pywsgi.py

from gevent import monkey
monkey.patch_all()

import os
from gevent.pywsgi import WSGIServer
from app import app

http_server = WSGIServer(('0.0.0.0', 8000), app)
http_server.serve_forever()
