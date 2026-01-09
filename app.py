from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained ML model
# Ensure the model is trained and saved as 'stroke_model.pkl'
MODEL_PATH = 'stroke_model.pkl'
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

# Map gender to numeric values (assuming this preprocessing was used in the model)
def preprocess_input(data):
    gender_map = {'Male': 0, 'Female': 1}
    gender = gender_map.get(data['gender'], 0)
    features = [
        data['age'],
        gender,
        data['bmi'],
        data['avg_glucose_level'],
        data['hypertension'],
        data['heart_disease'],
    ]
    return np.array(features).reshape(1, -1)

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON request
        input_data = request.get_json()

        # Preprocess the input
        features = preprocess_input(input_data)

        # Make prediction
        prediction = model.predict(features)
        probability = model.predict_proba(features)[0][1]  # Assuming a probability is available

        # Return the prediction as a JSON response
        result = {
            'prediction': int(prediction[0]),  # 1 for stroke, 0 for no stroke
            'probability': probability,
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
