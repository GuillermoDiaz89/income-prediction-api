
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
import joblib
import os

# Loading data

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
column = ['age', 'workclass', 'fnlwgt', 'education', 'education_num',
           'marital_status', 'occupation', 'relationship', 'race', 'sex',
           'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']

df = pd.read_csv(url, names=column, na_values= "?", skipinitialspace=True).dropna()

# Convert text to numeric
for col in df.select_dtypes(include=['object']).columns:
    df[col] = LabelEncoder().fit_transform(df[col])

x = df.drop('income', axis=1)
y = df['income']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = xgb.XGBClassifier()
model.fit(x_train, y_train)

# Create 'model' directory if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save the model
joblib.dump(model, "model/income_model.pkl")
print("✅ Model trained and saved")


