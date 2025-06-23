# 🧠 Income Prediction API (FastAPI + XGBoost)

![Python application](https://github.com/GuillermoDiaz89/income-prediction-api/actions/workflows/python-app.yml/badge.svg?branch=master)

This project is a RESTful API that predicts whether a person earns more or less than $50K based on census data. It uses an XGBoost model and is built with FastAPI.

---

## 🚀 How to Run

1. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   This command installs all required packages listed in `requirements.txt`.

3. **Train the model:**

   ```bash
   python train_model.py
   ```

   This script trains an XGBoost model using the adult census dataset.
   You can change the dataset URL inside `train_model.py`.

4. **Run the API server:**

   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
   Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

5. **Test the API via terminal (optional):**

   ```bash
   curl -X POST http://127.0.0.1:8000/predict \
   -H "Content-Type: application/json" \
   -d "{\"age\": 37, \"workclass\": 4, \"fnlwgt\": 284582, \"education\": 9, \"education_num\": 13, \"marital_status\": 2, \"occupation\": 2, \"relationship\": 1, \"race\": 4, \"sex\": 1, \"capital_gain\": 0, \"capital_loss\": 0, \"hours_per_week\": 40, \"native_country\": 38}"
   ```

---

## 🧪 Example Input (JSON)

```json
{
  "age": 37,
  "workclass": 4,
  "fnlwgt": 284582,
  "education": 9,
  "education_num": 13,
  "marital_status": 2,
  "occupation": 2,
  "relationship": 1,
  "race": 4,
  "sex": 1,
  "capital_gain": 0,
  "capital_loss": 0,
  "hours_per_week": 40,
  "native_country": 38
}
```

---

## 🧰 Tech Stack

- **FastAPI** – API framework  
- **XGBoost** – Model training  
- **Pandas & Scikit-learn** – Data preprocessing  
- **Joblib** – Model persistence  
- **Uvicorn** – ASGI server for FastAPI  
- **Pydantic** – Input validation

---

## 📂 Project Structure

```
.
├── app/
│   ├── main.py           # FastAPI app definition
│   └── model.py          # Model loading logic
├── model/
│   └── income_model.pkl  # Trained model
├── train_model.py        # Script to train and save model
├── test_client.py        # Test script to call the API
├── requirements.txt
├── setup.ps1             # Setup + API launcher script
├── .gitignore
└── README.md
```

---

## 📌 Author

Made by **Guillermo Díaz** — DevOps & Python Developer  
Feel free to fork or contribute 🚀


