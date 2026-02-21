from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load model and scaler
model = joblib.load('model/stroke_prediction_model.pkl')
scaler = joblib.load('model/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    age = float(data['age'])
    gender = 1 if data['gender'] == 'Male' else 0
    bmi = float(data['bmi'])
    glucose_level = float(data['avg_glucose_level'])
    hypertension = int(data['hypertension'])
    heart_disease = int(data['heart_disease'])

    features = np.array([[age, gender, bmi, glucose_level, hypertension, heart_disease]])

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)

    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)