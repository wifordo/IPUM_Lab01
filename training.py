import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


def load_data():
    return load_iris(return_X_y=True)


def train_model(X, y):
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model


def save_model(model):
    joblib.dump(model, "iris_model.joblib")


if __name__ == "__main__":
    X, y = load_data()
    clf = train_model(X, y)
    save_model(clf)
    print("Model wytrenowany i zapisany jako iris_model.joblib")
