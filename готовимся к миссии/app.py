from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title='Заготовка'):
    params = {
        'title': title,
        'heading': 'Миссия Колонизация Марса',
        'subheading': 'И на Марсе будут яблони цвести!'
    }
    return render_template('base.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')