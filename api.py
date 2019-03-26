import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


books = [
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'start': 'With a clamor of bells that set the swallows soaring...',
     'published': '1973'}]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to Titanic Predictor</h1>
<p>A prototype API for predicting who survives the Titanic.</p>'''


@app.route('/books', methods=['POST'])
def add_one():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify({'books': books})


app.run()
