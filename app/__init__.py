# app/__init.py

import magic
from flask import Flask, request, render_template, url_for
from datetime import datetime

app = Flask(__name__)
app.config.from_object('app.config')


@app.route('/', methods=['GET', 'POST'])
def index():
    args = {'now_year': datetime.now().year}
    if request.method == 'POST':
        f_chunk = request.files['file'].read(app.config['CHUNK_SIZE'])
        if f_chunk:
            args['f_magic'] = magic.from_buffer(f_chunk)
            args['f_mime'] = magic.from_buffer(f_chunk, mime=True)
    return render_template('layout.html', args=args)
