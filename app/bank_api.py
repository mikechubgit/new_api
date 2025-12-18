# Import packages
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path
import json
from xgboost import XGBClassifier


# Instantiate the app
app = FastAPI()

# Load the trained model
# Set the base directory as the folder where this program is located.
BASE_DIR = Path(__file__).parent

model_path = BASE_DIR / 'bankmarketing_best_model.pkl'
model = joblib.load(model_path)

# Load the best threshold
threshold_path = BASE_DIR / 'bankmarketing_best_model_best_threshold.json'

with open(threshold_path, 'r') as fh:
    threshold_dic = json.load(fh)

best_threshold = threshold_dic['best_threshold']

# Define input schema
class InputData(BaseModel):
    data: dict

# Root route 
@app.get('/')
def root():
    return{'message': 'Bank Marketing Model API is still running'}

# Prediction route
@app.post('/predict/')
def predict(input: InputData):
    # Convert dict to DataFrame
    df = pd.DataFrame([input.data])
    
    # Predict probability
    probability = float(model.predict_proba(df)[0][1])

    # Apply the best threshold
    prediction = int(probability >= best_threshold)

    return{
        'prediction': prediction,
        'probability': round(probability, 4),
        'threshold': round(best_threshold, 4)
    }
