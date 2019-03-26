import pickle
import numpy as np


class Model:

    def __init__(self):
        with open('model/model.pickle', 'rb') as f:
            self._model = pickle.load(f)

    def list_params(self):
        params = dict()
        params['Pclass'] = [1, 2, 3]
        params['Sex'] = [1, 0]
        params['Age'] = range(100)
        params['SibSp'] = [1, 0, 3, 4, 2, 5, 8]
        params['Parch'] = [0, 1, 2, 5, 3, 4, 6]
        params['Embarked'] = [0, 1, 2, 3]
        params['level'] = [8, 2, 4, 6, 3, 0, 1, 5, 7]

        return params

    def predict(self, lst):
        return self._model.predict(np.array([lst, ]))
