# 🩸 HemoScan AI – Anemia Detection & Clinical Interpretation System

HemoScan AI is a Machine Learning–powered Clinical Decision Support System designed to detect, classify, and interpret anemia using Complete Blood Count (CBC) parameters.

The system combines predictive modeling with rule-based clinical reasoning to provide structured medical insights beyond simple binary classification.

---

## 🚀 Key Features

- ✅ ML-Based Anemia Prediction (XGBoost)
- 📊 Risk Probability Scoring
- 🟢🟠🔴 Color-Coded Risk Dashboard
- 🩺 Severity Grading (Mild / Moderate / Severe)
- 🔬 Morphological Classification
  - Microcytic
  - Normocytic
  - Macrocytic
- 📖 Clinical Interpretation
- 🧠 Structured Medical Recommendations
- 🎨 Responsive & Modern UI

---

## 🧠 What Makes This Different?

Unlike basic classifiers, HemoScan AI provides:

- Hemoglobin-based severity grading
- MCV-based anemia morphology detection
- Etiological insights
- Clinical action guidance
- Lifestyle recommendations

This transforms the system from a simple ML model into a healthcare decision-support tool.

---

## 📥 Input Parameters

The system accepts the following CBC values:

- Gender  
- Hemoglobin (g/dL)  
- MCH (pg)  
- MCHC (g/dL)  
- MCV (fL)

---

## 🛠 Tech Stack

### Backend
- Python
- Flask
- Pandas
- Scikit-learn
- XGBoost
- Joblib

### Frontend
- HTML
- CSS
- Responsive UI Design

---

## 📁 Project Structure

```
HemoScan-AI/
│
├── app.py
├── models/
│   ├── xgboost_model.pkl
│   └── scaler.pkl
├── Dataset/
│   └── anemia.csv
├── templates/
│   └── index.html
├── static/
│   └── images/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sahananalla/HemoScan-AI.git
cd HemoScan-AI
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

Open in your browser:

```
http://127.0.0.1:5000/
```

---

## 📊 Model Information

- Algorithm: XGBoost Classifier
- Features standardized using StandardScaler
- Cross-validation performed
- Designed for early anemia risk detection

---

## 🎯 Use Cases

- Routine blood test screening
- Hospital triage assistance
- Community health programs
- Educational AI demonstrations

---

## ⚠️ Disclaimer

HemoScan AI is developed for educational and research purposes only.  
It does not replace professional medical diagnosis or treatment.

---

## 👩‍💻 Author

**Sahana Nalla**  
AI & Healthcare Enthusiast
