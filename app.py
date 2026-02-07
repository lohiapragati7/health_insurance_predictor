
import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))

st.title("Insurance Cost Predictor")

st.write("Enter details to estimate your insurance cost")

age = st.number_input("Age", 18, 100)
bmi = st.number_input("BMI", 10.0, 50.0)
children = st.number_input("Children", 0, 10)
smoker = st.selectbox("Smoker", ["Yes", "No"])

smoker = 1 if smoker == "Yes" else 0

if st.button("Predict"):
    input_data = pd.DataFrame([[age, bmi, children, smoker]])
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: ${round(prediction[0], 2)}")
