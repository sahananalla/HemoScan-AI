from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# ===== Load Model & Scaler =====
MODEL_PATH = os.path.join("models", "xgboost_model.pkl")
SCALER_PATH = os.path.join("models", "scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# ===== Routes =====

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    try:
        gender = float(request.form["gender"])
        hemoglobin = float(request.form["hemoglobin"])
        mch = float(request.form["mch"])
        mchc = float(request.form["mchc"])
        mcv = float(request.form["mcv"])

        features = np.array([[gender, hemoglobin, mch, mchc, mcv]])

        # Scale input
        scaled = scaler.transform(features)

        # Predict
        prediction = model.predict(scaled)[0]
        probability = model.predict_proba(scaled)[0][1]

        if prediction == 1:
            result_text = "⚠ Anemia Detected"
        else:
            result_text = "✓ No Anemia Detected"

        return render_template(
            "index.html",
            prediction_text=result_text,
            probability_text=f"Risk Probability: {probability*100:.2f}%",
            ai_suggestions="(Gemini integration will appear here)"
        )

    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
