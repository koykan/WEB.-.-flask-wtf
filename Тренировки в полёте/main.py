from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    prof_type = "engineering" if "инженер" in prof.lower() or "строитель" in prof.lower() else "science"

    return render_template('training.html', prof_type=prof_type, profession=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')