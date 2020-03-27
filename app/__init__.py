# app/__init.py

import magic
from flask import Flask, flash, request, redirect, render_template, url_for
from datetime import datetime

app = Flask(__name__)
app.config.from_object('app.config')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if not request.files.get('file', None):
            flash('You did not select a file to upload', 'danger')
            return redirect(request.url)
        f_chunk = request.files['file'].read(app.config['CHUNK_SIZE'])
        if f_chunk:
            magic_f = magic.from_buffer(f_chunk)
            flash(f'You file is: {magic_f}.', 'success')
    return render_template('layout.html', year=datetime.now().year)
