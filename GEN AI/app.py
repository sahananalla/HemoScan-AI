from flask import Flask, render_template, request
import joblib
import os
import pandas as pd

app = Flask(__name__)

# =========================================
# Load Model & Scaler
# =========================================

MODEL_PATH = os.path.join("models", "xgboost_model.pkl")
SCALER_PATH = os.path.join("models", "scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# =========================================
# Home Route
# =========================================

@app.route("/")
def home():
    return render_template("index.html")

# =========================================
# Prediction Route
# =========================================

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # ===== Get Form Data =====
        gender = float(request.form["gender"])
        hemoglobin = float(request.form["hemoglobin"])
        mch = float(request.form["mch"])
        mchc = float(request.form["mchc"])
        mcv = float(request.form["mcv"])

        # ===== Create DataFrame (must match training column names exactly) =====
        features = pd.DataFrame(
            [[gender, hemoglobin, mch, mchc, mcv]],
            columns=["Gender", "Hemoglobin", "MCH", "MCHC", "MCV"]
        )

        # ===== Scale Input =====
        scaled = scaler.transform(features)

        # ===== Predict =====
        prediction = model.predict(scaled)[0]
        probability = model.predict_proba(scaled)[0][1]
        risk_percent = probability * 100

        # =========================================
        # Result Text
        # =========================================
        if prediction == 1:
            result_text = "⚠ Anemia Detected"
        else:
            result_text = "✓ No Anemia Detected"

        # =========================================
        # Risk Level Classification
        # =========================================
        if risk_percent < 30:
            risk_level = "Low Risk"
            card_class = "low"
        elif risk_percent < 70:
            risk_level = "Moderate Risk"
            card_class = "moderate"
        else:
            risk_level = "High Risk"
            card_class = "high"



        # =========================================
        # Severity Classification (Hb Based)
        # =========================================
        severity = "Normal"

        if prediction == 1:
            if hemoglobin < 8:
                severity = "Severe Anemia"
            elif hemoglobin < 10:
                severity = "Moderate Anemia"
            else:
                severity = "Mild Anemia"

        # =========================================
        # MCV-Based Morphology Classification
        # =========================================
        anemia_type = "Not Applicable"
        interpretation = "No clinical signs of anemia detected."

        if prediction == 1:
            if mcv < 80:
                anemia_type = "Microcytic Anemia"
                interpretation = "Most commonly associated with Iron Deficiency."
            elif 80 <= mcv <= 100:
                anemia_type = "Normocytic Anemia"
                interpretation = "May indicate acute blood loss or chronic disease."
            else:
                anemia_type = "Macrocytic Anemia"
                interpretation = "Often linked to Vitamin B12 or Folate deficiency."

        # =========================================
        # Clinical Recommendation
        # =========================================
        if prediction == 1:
            ai_suggestions = f"""
            Clinical Summary:
            Patient classified as {severity} with {anemia_type} morphology.

            Recommended Actions:
            • Immediate physician consultation advised.
            • Nutritional assessment recommended.
            • Further laboratory evaluation may be required.
            """
        else:
            ai_suggestions = """
            CBC parameters fall within normal clinical range.

            Recommendations:
            • Maintain balanced diet.
            • Routine health check-up advised.
            """

        # =========================================
        # Render Result
        # =========================================
        return render_template(
    "index.html",
    prediction_text=result_text,
    probability_text=f"{risk_percent:.2f}%",
    risk_level=risk_level,
    severity=severity,
    anemia_type=anemia_type,
    interpretation=interpretation,
    ai_suggestions=ai_suggestions,
    card_class=card_class
)


    except Exception as e:
        return render_template(
            "index.html",
            prediction_text="Error occurred during prediction.",
            probability_text=str(e)
        )

# =========================================
# Run Application
# =========================================

if __name__ == "__main__":
    app.run(debug=True)
