# 🎓 Student Marks Predictor

A machine learning project that predicts a student's exam score based on academic and lifestyle-related factors.

## 🚀 Live Demo

Want to try the application yourself?

👉 **[Live Demo – Student Marks Predictor](https://student-marks-predictor-ai.streamlit.app/)**

Open the link above to use the deployed Streamlit application and get a predicted exam score.

## 📌 Project Overview

This project predicts student exam scores using machine learning.

The project includes:

- Data preprocessing
- Exploratory data analysis
- Multiple regression models
- Model comparison
- Hyperparameter tuning using RandomizedSearchCV
- Model serialization using Pickle/Joblib
- Interactive Streamlit frontend
- Deployment as a live web application

## 🤖 Machine Learning Models

Two major regression models were compared:

- Random Forest Regressor
- Gradient Boosting Regressor

After comparing their performance using R², MAE, RMSE and Cross-Validation, **Gradient Boosting Regressor** was selected as the final model.

## 📊 Input Features

The model uses:

- Study Hours
- Attendance
- Sleep Hours
- Internet Usage
- Assignment Completion
- Previous Score

## 📈 Model Performance

The final Gradient Boosting model achieved approximately:

- **Test R²: 0.73**
- **Cross-Validation R²: ~0.71**

The model was further tuned using `RandomizedSearchCV`.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib / Pickle
- Streamlit

## 🌐 Deployment

The application is deployed using Streamlit and is available as a live web application.

👉 **[Try the Live Demo](https://student-marks-predictor-ai.streamlit.app/)**

## 📁 Project Structure

```text
student-marks-predictor/
│
├── app.py
├── student_marks_model.pkl
├── requirements.txt
└── README.md
