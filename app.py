import streamlit as st
import pandas as pd
import pickle

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Health Insurance Charge Estimator",
    page_icon="💰",
    layout="wide"
)

# ----------------------------
# Load Model
# ----------------------------
model = pickle.load(open("model.pkl", "rb"))

# ----------------------------
# Title
# ----------------------------
st.title("💰Health Insurance Charges Estimator")
st.markdown("### Predict medical insurance claim amount instantly")
st.markdown("---")


# ============================
# INPUT SECTION
# ============================

st.header("🧍 Personal Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 18, 100, 30)

with col2:
    sex = st.selectbox("Sex", ["male", "female"])

with col3:
    children = st.number_input("Children", 0, 10, 0)


st.header("🏥 Health & Lifestyle")

col4, col5, col6 = st.columns(3)

with col4:
    bmi = st.number_input("BMI", 10.0, 50.0, 25.0)

with col5:
    smoker = st.selectbox("Smoker", ["Yes", "No"])

with col6:
    num_of_steps = st.number_input("Daily Steps", 0, 50000, 5000)


st.header("📋 Medical History")

col7, col8, col9 = st.columns(3)

with col7:
    past_consultations = st.number_input("Past Consultations", 0, 50, 2)

with col8:
    hospital_exp = st.number_input("Hospital Expenditure", 0.0, 1000000.0, 1000.0)

with col9:
    past_hospitalizations = st.number_input("Past Hospitalizations", 0, 20, 0)


st.header("💼 Financial & Location")

col10, col11, col12 = st.columns(3)

with col10:
    salary = st.number_input("Annual Salary", 0.0, 10000000.0, 300000.0)

with col11:
    region = st.selectbox(
        "Region",
        ["northeast", "northwest", "southeast", "southwest"]
    )

with col12:
    claim_amount = st.number_input("Previous Claim Amount", 0.0, 1000000.0, 0.0)


st.markdown("---")


# ============================
# ENCODING
# ============================

sex = 1 if sex == "male" else 0
smoker = 1 if smoker == "Yes" else 0

region_map = {
    "northeast": 0,
    "northwest": 1,
    "southeast": 2,
    "southwest": 3
}

region = region_map[region]


# ============================
# PREDICTION
# ============================

if st.button(" Predict Health Insurance Charges", use_container_width=True):

    input_data = pd.DataFrame([[
        age,
        sex,
        bmi,
        children,
        smoker,
        claim_amount,
        past_consultations,
        num_of_steps,
        hospital_exp,
        past_hospitalizations,
        salary,
        region
    ]])

    prediction = max(model.predict(input_data)[0], 0)

    st.success(f"### 💵 Estimated Charges: ₹ {round(prediction, 2)}")
    st.balloons()


# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Built with Streamlit • Scikit-learn • Python")


