import streamlit as st
import joblib

model = joblib.load("Student_marks_model.pkl")

st.title("🎓 Student Marks Predictor")

study_hours = st.number_input("Study Hours", min_value=0.0)
attendance = st.number_input("Attendance", min_value=0.0, max_value=100.0)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0)
internet_usage = st.number_input("Internet Usage", min_value=0.0)
assignment_completed = st.number_input(
    "Assignment Completion",
    min_value=0.0,
    max_value=100.0
)
previous_score = st.number_input(
    "Previous Score",
    min_value=0.0,
    max_value=100.0
)

if st.button("Predict Score"):

    input_data = [[
        study_hours,
        attendance,
        sleep_hours,
        internet_usage,
        assignment_completed,
        previous_score
    ]]

    prediction = model.predict(input_data)

    st.success(f"Predicted Exam Score: {prediction[0]:.2f}")