import joblib
import numpy as np

model = joblib.load("models/xgboost_model.pkl")
scaler = joblib.load("models/scaler.pkl")

def predict_anemia(data):
    features = np.array([data])
    scaled = scaler.transform(features)

    prediction = model.predict(scaled)[0]
    probability = model.predict_proba(scaled)[0][1]

    return prediction, probability
