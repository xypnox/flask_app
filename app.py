from flask import Flask, render_template, request

app = Flask(__name__)
poem_data = []


@app.route('/')
def Index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/poems')
def articles():
    return render_template('poems.html', poems=poem_data)


@app.route('/submit', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        print(result)
        return render_template('submit.html')
    else:
        return render_template('submit.html')


if __name__ == '__main__':
    app.run(debug=True)
