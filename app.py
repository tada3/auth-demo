# app.py

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_page():
    return render_template('index.html', title='Home')

@app.route('/reverse', methods=['GET', 'POST'])
def reverse_word():
    reversed_word = ''
    if request.method == 'POST':
        word = request.form['word']
        reversed_word = word[::-1]
    return render_template('reverse.html', reversed_word=reversed_word)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
