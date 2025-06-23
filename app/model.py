import joblib

model = joblib.load("model/income_model.pkl")

def load_model_and_predict(data):
    return model.predict(data)