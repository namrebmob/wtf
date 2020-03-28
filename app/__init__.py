# app/__init.py

import magic
from flask import Flask, flash, request, redirect, render_template, url_for
from datetime import datetime

app = Flask(__name__)
app.config.from_object('app.config')


@app.route('/', methods=['GET', 'POST'])
def index():
    args = {'charset': request.charset, 'year': datetime.now().year}
    if request.method == 'POST':
        if not request.files.get('file', None):
            flash('You did not select a file to upload', 'danger')
            return redirect(request.url)
        magic_f = magic.from_buffer(request.files['file'].read(2048))
        flash(f'You file is {magic_f}.', 'success')
    return render_template('layout.html', args=args)
