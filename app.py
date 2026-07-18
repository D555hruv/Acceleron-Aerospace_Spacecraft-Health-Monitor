import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# ----------------------------
# Load AI Model
# ----------------------------
model = joblib.load("models/health_model.pkl")

st.set_page_config(page_title="Spacecraft Health Monitor", layout="wide")

st.title("🛰️ AI-Based Spacecraft Health Monitoring System")
st.write("Software Simulation using Machine Learning")

st.divider()

# ----------------------------
# Generate Live Telemetry
# ----------------------------
if st.button("Generate Live Telemetry"):

    telemetry = {
        "Battery_Voltage": np.random.uniform(22,30),
        "Battery_Current": np.random.uniform(1,8),
        "Temperature": np.random.uniform(15,80),
        "CPU_Load": np.random.uniform(10,100),
        "Signal_Strength": np.random.uniform(40,100),
        "Fuel_Level": np.random.uniform(20,100)
    }

    df = pd.DataFrame([telemetry])

    prediction = model.predict(df)[0]

    col1,col2,col3 = st.columns(3)

    col1.metric("Battery Voltage", f"{telemetry['Battery_Voltage']:.2f} V")
    col2.metric("Temperature", f"{telemetry['Temperature']:.2f} °C")
    col3.metric("CPU Load", f"{telemetry['CPU_Load']:.2f} %")

    col4,col5,col6 = st.columns(3)

    col4.metric("Battery Current", f"{telemetry['Battery_Current']:.2f} A")
    col5.metric("Signal Strength", f"{telemetry['Signal_Strength']:.2f} %")
    col6.metric("Fuel Level", f"{telemetry['Fuel_Level']:.2f} %")

    st.subheader("AI Prediction")

    if prediction == "Healthy":
        st.success("🟢 Healthy")
    elif prediction == "Warning":
        st.warning("🟡 Warning")
    else:
        st.error("🔴 Critical")

    fig = px.bar(
        x=df.columns,
        y=df.iloc[0],
        title="Current Spacecraft Telemetry"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Historical Dataset")

history = pd.read_csv("telemetry.csv")

st.dataframe(history.head())

fig2 = px.scatter(
    history,
    x="Temperature",
    y="Battery_Voltage",
    color="Health"
)

st.plotly_chart(fig2, use_container_width=True)
