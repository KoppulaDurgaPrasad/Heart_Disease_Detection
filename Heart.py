import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)


st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

div.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}

[data-testid="stMetric"] {
    background-color: #1E1E1E;
    padding: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


model = joblib.load("Logistic_Regression.pkl")
scaler = joblib.load("scaler.pkl")
cols = joblib.load("columns.pkl")


st.sidebar.title("🫀 Model Information")
st.sidebar.success("Algorithm: Logistic Regression")
st.sidebar.info("Accuracy: 86.41%")
st.sidebar.write("Problem Type: Binary Classification")
st.sidebar.write("Output Classes:")
st.sidebar.write("• 0 → Low Risk")
st.sidebar.write("• 1 → High Risk")


st.markdown("""
<div style='text-align:center; font-size:70px;'>
🫀
</div>

<h1 style='text-align:center; color:#ff4b4b;'>
Heart Disease Prediction
</h1>

<p style='text-align:center; color:gray; font-size:18px;'>
Predict the likelihood of heart disease using Machine Learning
</p>
""", unsafe_allow_html=True)

st.divider()

st.subheader("🩺 Patient Information")

age = st.slider("Age", 18, 100, 40)

sex = st.selectbox(
    "Sex",
    ["M", "F"]
)

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "TA", "ASY"]
)

resting_bp = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=80,
    max_value=200,
    value=120
)

cholesterol = st.number_input(
    "Cholesterol (mg/dL)",
    min_value=100,
    max_value=600,
    value=200
)

fasting_bs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dL",
    [0, 1]
)

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)

max_hr = st.slider(
    "Maximum Heart Rate",
    60,
    220,
    150
)

exercise_angina = st.selectbox(
    "Exercise-Induced Angina",
    ["Y", "N"]
)

oldpeak = st.slider(
    "Oldpeak (ST Depression)",
    0.0,
    6.0,
    1.0
)

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)

st.subheader("📋 Patient Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Age", age)

with col2:
    st.metric("BP", resting_bp)

with col3:
    st.metric("Cholesterol", cholesterol)

st.divider()

if st.button("🔍 Predict Heart Disease Risk", use_container_width=True):

    with st.spinner("Analyzing patient data..."):

        raw_input = {
            "Age": age,
            "RestingBP": resting_bp,
            "Cholesterol": cholesterol,
            "FastingBS": fasting_bs,
            "MaxHR": max_hr,
            "Oldpeak": oldpeak,
            "Sex_" + sex: 1,
            "ChestPainType_" + chest_pain: 1,
            "RestingECG_" + resting_ecg: 1,
            "ExerciseAngina_" + exercise_angina: 1,
            "ST_Slope_" + st_slope: 1
        }

        input_df = pd.DataFrame([raw_input])

        for c in cols:
            if c not in input_df.columns:
                input_df[c] = 0

        input_df = input_df[cols]

        scaled_input = scaler.transform(input_df)

        prediction = model.predict(scaled_input)[0]

        probability = model.predict_proba(scaled_input)[0][1]

        risk_percent = probability * 100

        st.subheader("📊 Risk Assessment")

        st.progress(int(risk_percent))

        if risk_percent > 70:
            st.error(f"Risk Probability: {risk_percent:.2f}%")
        elif risk_percent > 40:
            st.warning(f"Risk Probability: {risk_percent:.2f}%")
        else:
            st.success(f"Risk Probability: {risk_percent:.2f}%")

        if prediction == 1:
            st.error(
                f"⚠️ High Risk of Heart Disease ({risk_percent:.2f}% confidence)"
            )
        else:
            st.success(
                f"✅ Low Risk of Heart Disease ({100 - risk_percent:.2f}% confidence)"
            )
            st.balloons()

st.markdown("---")

st.markdown("""
<div style="
text-align:center;
padding:20px;
border-radius:15px;
background: linear-gradient(90deg, #1E1E1E, #2D2D2D);
color:white;
font-size:16px;
">
❤️ Developed by Durga Prasad<br>
Heart Disease Prediction System<br>
Logistic Regression • Accuracy: 86.41%
</div>
""", unsafe_allow_html=True)