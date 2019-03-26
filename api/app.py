
from flask import request
from flask_api import FlaskAPI
# from ../model import Model, allowed_values


app = FlaskAPI(__name__)


@app.route("/titanic", methods=['GET', 'POST'])
def titanic():
    if request.method == 'POST':
        return "Sweet request man!"
    else:
        return "Fuck Off!"


@app.route("/", methods=['GET'])
def index():
    return "Hey Guys!"


if __name__ == "__main__":
    app.run(debug=True)
