import joblib
from sklearn.datasets import load_iris


def load_model():
    return joblib.load("iris_model.joblib")


def predict(model, data):
    iris = load_iris()
    # model.predict oczekuje listy list [[...]]
    prediction = model.predict([list(data.values())])
    return iris.target_names[prediction[0]]
