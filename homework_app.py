# homework_app.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from homework_inference import load_model, predict as make_prediction

app = FastAPI(title="Sentiment Analysis Inference API")

# Ładowanie modeli raz przy starcie aplikacji
models = load_model()

class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1)

class PredictResponse(BaseModel):
    prediction: str

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    res = make_prediction(models, request.text)
    return PredictResponse(prediction=res)
