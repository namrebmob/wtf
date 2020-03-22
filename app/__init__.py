import magic, mimetypes
from flask import Flask, request, render_template, url_for
from datetime import datetime

app = Flask(__name__)

app.config.from_envvar('SECRET_KEY')
app.config.from_envvar('MAGIC_CONTENT_LENGTH')


@app.route('/', methods=['GET', 'POST'])
def home():
    args = {'method': 'GET'}
    if request.method == 'POST':
        file = request.files['file']
        if file:
            f = magic.Magic(uncompress=True)
            args['file_data'] = f.from_buffer(file.read(app.config['MAGIC_CONTENT_LENGTH']))
            args['mime_type'], args['encoding'] = mimetypes.guess_type(file.filename, strict=False)
    return render_template('home.html', args=args)
