import os
import joblib
from sentence_transformers import SentenceTransformer


def load_model():
    # Ładowanie modeli
    transformer_path = os.path.join("sentiment_model", "sentence_transformer")
    reg_path = os.path.join("sentiment_model", "logistic_regression.joblib")

    transformer = SentenceTransformer(transformer_path)
    reg_model = joblib.load(reg_path)
    return transformer, reg_model


def predict(models, text: str) -> str:
    transformer, reg_model = models

    # Zamiana tekstu na wektor (embedding)
    embedding = transformer.encode([text])

    # Klasyfikacja regresją logistyczną
    pred_id = reg_model.predict(embedding)

    # Mapowanie wyniku
    label_map = {0: "negative", 1: "neutral", 2: "positive"}
    return label_map.get(pred_id[0], "unknown")
