from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index/<title>')
def index(title='Заготовка'):
    return render_template('base.html', title=title)


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index', title='Фото загружено'))
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
