from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from app.model import load_model_and_predict

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
