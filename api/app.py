
from flask import request, abort
from flask_api import FlaskAPI
from model.model import Model

# from . import Model, allowed_values


app = FlaskAPI(__name__)
model_a = Model()
allowed_params = set(model_a.list_params().keys())


@app.route("/titanic", methods=['GET', 'POST'])
def titanic():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        else:
            data = request.json
            if set(data.keys()) != allowed_params:
                abort(403)
            else:
                result = model_a.predict(list(data.values()))[0]
                if result == 1:
                    return 'Survived'
                else:
                    return 'Dead'
    else:
        abort(418)


@app.route("/", methods=['GET'])
def index():
    return "Hey Guys!"


if __name__ == "__main__":
    app.run(debug=True)
