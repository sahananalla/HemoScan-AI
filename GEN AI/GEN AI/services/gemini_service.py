import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")

def generate_suggestions(patient_data, prediction, probability):
    
    prompt = f"""
    A patient has the following blood parameters:
    Hemoglobin: {patient_data['hemoglobin']}
    MCH: {patient_data['mch']}
    MCHC: {patient_data['mchc']}
    MCV: {patient_data['mcv']}
    Risk Probability: {probability*100:.2f}%

    Provide:
    1. Clinical explanation in simple language
    2. Lifestyle suggestions
    3. Dietary advice
    4. When to consult doctor

    Keep response structured and concise.
    """

    response = model.generate_content(prompt)
    return response.text
