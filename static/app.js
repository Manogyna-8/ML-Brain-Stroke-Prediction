document.getElementById('stroke-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const data = {
        age: document.getElementById('age').value,
        gender: document.getElementById('gender').value,
        bmi: document.getElementById('bmi').value,
        avg_glucose_level: document.getElementById('glucose-level').value,
        hypertension: document.getElementById('hypertension').value,
        heart_disease: document.getElementById('heart-disease').value
    };

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML =
            'Prediction: ' + (data.prediction === 1 ? 'Stroke' : 'No Stroke');
    })
    .catch(error => console.error('Error:', error));
});