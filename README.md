# 🎓 Student Marks Predictor

A machine learning project that predicts a student's exam score based on academic and lifestyle-related factors.

The project uses a Gradient Boosting Regressor and provides an interactive web interface built with Streamlit.

## 🚀 Features

- Predicts student exam scores
- Interactive Streamlit interface
- Uses multiple student-related features
- Machine learning model comparison
- Hyperparameter tuning using RandomizedSearchCV
- Model evaluation using R², MAE and RMSE

## 📊 Input Features

The model uses the following features:

- Study Hours
- Attendance
- Sleep Hours
- Internet Usage
- Assignment Completion
- Previous Score

## 🤖 Machine Learning

Several regression algorithms were evaluated, including:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

After comparison and hyperparameter tuning, Gradient Boosting Regressor was selected as the final model.

## 📈 Model Evaluation

The final model was evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Cross-validation

The final model achieved approximately:

- Test R²: 0.73

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## 📁 Project Structure

```text
student-marks-predictor/
│
├── app.py
├── student_marks_model.pkl
├── requirements.txt
└── README.md