import streamlit as st
import pandas as pd
import pickle

# ======================================
# Page Config
# ======================================
st.set_page_config(
    page_title="Insurance Charges Estimator",
    page_icon="💰",
    layout="wide"
)

# ======================================
# Load Model
# ======================================
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()


# ======================================
# Title
# ======================================
st.title("💰 Insurance Charges Estimator")
st.write("Predict medical insurance claim cost using Machine Learning")

st.divider()


# ======================================
# INPUT UI
# ======================================

st.subheader("👤 Personal Info")
c1, c2, c3 = st.columns(3)

with c1:
    age = st.number_input("Age", 18, 100, 30)

with c2:
    sex = st.selectbox("Sex", ["male", "female"])

with c3:
    children = st.number_input("Children", 0, 10, 0)


st.subheader("🏥 Health Details")
c4, c5, c6 = st.columns(3)

with c4:
    bmi = st.number_input("BMI", 10.0, 50.0, 25.0)

with c5:
    smoker = st.selectbox("Smoker", ["Yes", "No"])

with c6:
    num_of_steps = st.number_input("Daily Steps", 0, 50000, 5000)


st.subheader("📋 Medical History")
c7, c8, c9 = st.columns(3)

with c7:
    past_consultations = st.number_input("Past Consultations", 0, 50, 2)

with c8:
    hospital_exp = st.number_input("Hospital Expenditure", 0.0, 1_000_000.0, 1000.0)

with c9:
    past_hospitalizations = st.number_input("Past Hospitalizations", 0, 20, 0)


st.subheader("💼 Financial & Location")
c10, c11, c12 = st.columns(3)

with c10:
    salary = st.number_input("Annual Salary", 0.0, 10_000_000.0, 300000.0)

with c11:
    region = st.selectbox(
        "Region",
        ["northeast", "northwest", "southeast", "southwest"]
    )

with c12:
    claim_amount = st.number_input("Previous Claim Amount", 0.0, 1_000_000.0, 0.0)


st.divider()


# ======================================
# Encoding (same as training)
# ======================================

sex = 1 if sex == "male" else 0
smoker = 1 if smoker == "Yes" else 0

region_map = {
    "northeast": 0,
    "northwest": 1,
    "southeast": 2,
    "southwest": 3
}

region = region_map[region]


# ======================================
# Prediction
# ======================================

if st.button("🚀 Predict Charges", use_container_width=True):

    # SAFE METHOD → column names (prevents order bugs)
    input_data = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "Claim_Amount": claim_amount,
        "past_consultations": past_consultations,
        "num_of_steps": num_of_steps,
        "Hospital_expenditure": hospital_exp,
        "NUmber_of_past_hospitalizations": past_hospitalizations,
        "Anual_Salary": salary,
        "region": region
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"### 💵 Estimated Insurance Charges: ₹ {round(prediction, 2)}")
    st.balloons()


# ======================================
# Footer
# ======================================
st.divider()
st.caption("Built with ❤️ using Streamlit + Scikit-learn")




