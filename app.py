from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/poems')
def articles():
    return render_template('poems.html')


if __name__ == '__main__':
    app.run(debug=True)
