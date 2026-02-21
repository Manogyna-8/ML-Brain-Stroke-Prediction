# 🧠 Brain Stroke Prediction – Machine Learning Based Risk Assessment

## 📌 Overview
Brain Stroke Prediction is a Machine Learning–based web application that predicts the likelihood of stroke occurrence using clinical and demographic features.

The system applies supervised learning techniques to support early risk identification and preventive healthcare decision-making.

---

## 🚀 Features

- Stroke risk prediction using Logistic Regression & Decision Tree
- Data preprocessing (missing value imputation, encoding, scaling)
- 80–20 train-test validation split
- Confusion matrix & classification report generation
- Correlation heatmap visualization
- Flask-based real-time prediction interface
- Probability-based risk estimation

---

## 🏗 System Architecture

### Pipeline Flow

Data Collection → Preprocessing → Feature Engineering → Model Training → Evaluation → Deployment (Flask API)

### Core Components

- Data Preprocessing Module
- Feature Engineering Pipeline
- Logistic Regression Model
- Decision Tree Model
- Model Evaluation Engine
- Flask Web Interface

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Accuracy | 94.6% |
| Weighted F1-score | 0.92 |
| Prediction Response Time | < 2 seconds |

> ⚠️ Note: Model performance is influenced by class imbalance in the dataset.

---

## 📋 Features Used in Model

- Age
- BMI
- Average Glucose Level
- Hypertension
- Heart Disease
- Gender

---

## 🛠 Tech Stack

| Category | Tools Used |
|----------|------------|
| Backend | Python, Flask |
| Machine Learning | Scikit-learn (Logistic Regression, Decision Tree) |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Model Persistence | Joblib |

---

## 📁 Project Structure

```
ML-Brain-Stroke-Prediction/
│
├── data/
│   └── stroke_data.csv
│
├── model/                # (Ignored from Git)
│   ├── stroke_prediction_model.pkl
│   └── scaler.pkl
│
├── notebook/
│   └── Stroke_training.ipynb
│
├── static/
│   └── app.js
│
├── templates/
│   └── index.html
│
├── backend.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧪 How to Run Locally

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Train Model (If .pkl files not present)

Run the notebook:

```
notebook/Stroke_training.ipynb
```

This will generate:
- model/stroke_prediction_model.pkl
- model/scaler.pkl

### 3️⃣ Run Flask Application

```bash
python backend.py
```

### 4️⃣ Open in Browser

http://127.0.0.1:5000

---

## 🔮 Future Improvements

- Handle class imbalance using SMOTE
- Hyperparameter tuning
- Deploy using cloud services (Render / AWS)
- Add user authentication system
- Integrate database for patient history storage

---

## 👩‍💻 Author

Manogyna A
