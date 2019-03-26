import flask
# from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to Titanic Predictor</h1>
<p>A prototype API for predicting who survives the Titanic.</p>'''


app.run()
