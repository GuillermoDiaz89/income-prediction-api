from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pandas as pd
from app.model import load_model_and_predict
import os
import json

app = FastAPI()

# ✅ Ruta raíz para verificar que la API está corriendo
@app.get("/")
def read_root():
    return {"message": "API is running"}

class Person(BaseModel):
    age: int
    workclass: int
    fnlwgt: int
    education: int
    education_num: int
    marital_status: int
    occupation: int
    relationship: int
    race: int
    sex: int
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: int

@app.post("/predict")
def predict_income(person: Person):
    df = pd.DataFrame([person.model_dump()])
    prediction = load_model_and_predict(df)
    return {"prediction": "> $50K" if prediction[0] == 1 else "< $50K"}


@app.get("/metrics")
def get_metrics():
    metrics_path = "model/metrics.json"
    if not os.path.exists(metrics_path):
        return JSONResponse(status_code=404, content={"detail": "Metrics file not found."})
    
    with open(metrics_path, "r") as f:
        metrics = json.load(f)
    return metrics


@app.get("/importance")
def get_feature_importance_plot():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_path = os.path.join(base_path, "model", "feature_importance.png")

    if not os.path.exists(img_path):
        return JSONResponse(status_code=404, content={"detail": "Image not found."})

    return FileResponse(img_path, media_type="image/png")
