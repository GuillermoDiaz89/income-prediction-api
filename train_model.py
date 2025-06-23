import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import xgboost as xgb
import joblib
import json
import os
import matplotlib.pyplot as plt
from xgboost import plot_importance

# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num',
           'marital_status', 'occupation', 'relationship', 'race', 'sex',
           'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']

df = pd.read_csv(url, names=columns, na_values="?", skipinitialspace=True).dropna()

# Encode categorical columns
for col in df.select_dtypes(include=['object']).columns:
    df[col] = LabelEncoder().fit_transform(df[col])

x = df.drop('income', axis=1)
y = df['income']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train model
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(x_train, y_train)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/income_model.pkl")

# Evaluate model
y_pred = model.predict(x_test)
report = classification_report(y_test, y_pred, output_dict=True)

# Save metrics as JSON
with open("model/metrics.json", "w") as f:
    json.dump(report, f, indent=4)

# Plot feature importance
plt.figure(figsize=(10, 6))
plot_importance(model, max_num_features=10, importance_type='weight', title="Top 10 Feature Importances")
plt.tight_layout()
plt.savefig("model/feature_importance.png")
plt.close()
 
print("✅ Model trained and saved as model/income_model.pkl")
print("📊 Metrics saved as model/metrics.json")
print("📈 Feature importance plot saved as model/feature_importance.png")   