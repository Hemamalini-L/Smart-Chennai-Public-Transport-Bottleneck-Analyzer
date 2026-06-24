import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Smart Chennai Public Transport Analyzer",
    page_icon="🚌",
    layout="wide"
)

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------
@st.cache_resource
def load_model():
    with open("delay_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("🚌 Smart Chennai Public Transport Bottleneck Analyzer")
st.markdown(
    "AI-powered public transport analytics with real-time weather integration and delay prediction."
)

# ---------------------------------------------------
# WEATHER SECTION
# ---------------------------------------------------
st.subheader("🌦️ Chennai Real-Time Weather")

API_KEY = "YOUR_OPENWEATHER_API_KEY"

temperature = 32
humidity = 70
weather_desc = "Unavailable"

try:
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Chennai&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]

except:
    pass

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Temperature (°C)", round(temperature, 1))

with col2:
    st.metric("Humidity (%)", humidity)

with col3:
    st.metric("Condition", weather_desc.title())

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.header("Prediction Inputs")

hour = st.sidebar.slider(
    "Hour of Day",
    min_value=0,
    max_value=23,
    value=8
)

occupancy_rate = st.sidebar.slider(
    "Occupancy Rate (%)",
    min_value=0,
    max_value=100,
    value=60
)

temperature_input = st.sidebar.number_input(
    "Temperature (°C)",
    value=float(temperature)
)

humidity_input = st.sidebar.number_input(
    "Humidity (%)",
    value=float(humidity)
)

# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------
st.subheader("🚦 Delay Prediction")

input_data = pd.DataFrame({
    "hour": [hour],
    "occupancy_rate": [occupancy_rate],
    "temperature": [temperature_input],
    "humidity": [humidity_input]
})

predicted_delay = model.predict(input_data)[0]

st.metric(
    "Predicted Delay (Minutes)",
    round(predicted_delay, 2)
)

# ---------------------------------------------------
# RISK LEVEL
# ---------------------------------------------------
if predicted_delay < 5:
    risk = "LOW"
elif predicted_delay < 12:
    risk = "MEDIUM"
else:
    risk = "HIGH"

st.subheader("⚠️ Risk Assessment")

if risk == "LOW":
    st.success(f"Risk Level: {risk}")

elif risk == "MEDIUM":
    st.warning(f"Risk Level: {risk}")

else:
    st.error(f"Risk Level: {risk}")

# ---------------------------------------------------
# RECOMMENDATIONS
# ---------------------------------------------------
st.subheader("💡 Recommendations")

if risk == "LOW":
    st.info(
        """
        • Service operating normally  
        • Continue regular scheduling  
        • Monitor occupancy levels
        """
    )

elif risk == "MEDIUM":
    st.warning(
        """
        • Increase monitoring during peak hours  
        • Consider additional services  
        • Alert operations team
        """
    )

else:
    st.error(
        """
        • Deploy additional buses/trains  
        • Notify commuters of delays  
        • Optimize route scheduling  
        • Increase frequency immediately
        """
    )

# ---------------------------------------------------
# SIMULATION CHART
# ---------------------------------------------------
st.subheader("📈 Delay Trend Simulation")

hours = list(range(24))

sim_df = pd.DataFrame({
    "Hour": hours,
    "Predicted Delay": [
        model.predict(pd.DataFrame({
            "hour": [h],
            "occupancy_rate": [occupancy_rate],
            "temperature": [temperature_input],
            "humidity": [humidity_input]
        }))[0]
        for h in hours
    ]
})

fig = px.line(
    sim_df,
    x="Hour",
    y="Predicted Delay",
    title="Predicted Delay Across Different Hours"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.markdown(
    """
    Developed by **Hemamalini L**  
    B.Tech Artificial Intelligence and Data Science  
    Smart Chennai Public Transport Bottleneck Analyzer
    """
)
