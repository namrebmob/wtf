# app/__init.py

import magic
from flask import Flask, flash, request, redirect, render_template, url_for
from werkzeug.exceptions import RequestEntityTooLarge
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
        try:
            file = request.files.get('file').read(2048)
        except RequestEntityTooLarge:
            flash('File size too large. Limit is 16MB.', 'danger')
            return redirect(request.url)
        f_magic = magic.from_buffer(file)
        flash(f'You file is {f_magic}.', 'success')
    return render_template('layout.html', args=args)


@app.errorhandler(413)
def page_not_found(e):
    return "Your error page for 413 status code", 413
