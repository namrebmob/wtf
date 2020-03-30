# app/__init.py

import magic
from datetime import datetime
from flask import Flask, flash, request, redirect, render_template, url_for


app = Flask(__name__)
app.config.from_object('app.config.config')


@app.route('/', methods=['GET', 'POST'])
def index():
    args = {'charset': request.charset, 'year': datetime.now().year}
    if request.method == 'POST':
        if not request.files.get('file', None):
            flash('You did not select a file to upload', 'danger')
            return redirect(request.url)
        file = request.files.get('file').read(2048)
        if file:
            f_magic = magic.from_buffer(file)
            flash(f'You file is {f_magic}.', 'success')
            return redirect(request.url)
    return render_template('layout.html', args=args)

@app.errorhandler(413)
def request_entity_too_large(e):
    flash(f'{e}', 'danger')
    return redirect(request.url)
