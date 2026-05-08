from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse
from inference import load_model, predict as make_prediction

app = FastAPI()

# Globalne ładowanie modelu
model = load_model()


@app.get("/")
def read_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    # Używamy model_dump(), aby wyciągnąć dane z Pydantic
    res = make_prediction(model, request.model_dump())
    return PredictResponse(prediction=res)
