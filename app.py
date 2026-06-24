import streamlit as st
import pandas as pd
import plotly.express as px
import pickle

# ------------------------------
# PAGE CONFIG
# ------------------------------

st.set_page_config(
    page_title="Smart Chennai Public Transport Analyzer",
    page_icon="🚌",
    layout="wide"
)

# ------------------------------
# LOAD DATA
# ------------------------------

@st.cache_data
def load_data():
    dashboard = pd.read_csv("dashboard_data_sample.csv")
    kpis = pd.read_csv("dashboard_kpis.csv")
    route_delay = pd.read_csv("route_delay_analysis.csv")
    route_util = pd.read_csv("route_utilization.csv")
    stop_volume = pd.read_csv("stop_passenger_volume.csv")
    weather = pd.read_csv("weather_dataset.csv")

    return dashboard, kpis, route_delay, route_util, stop_volume, weather


dashboard, kpis, route_delay, route_util, stop_volume, weather = load_data()

# ------------------------------
# LOAD MODEL
# ------------------------------

@st.cache_resource
def load_model():
    with open("delay_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# ------------------------------
# SIDEBAR
# ------------------------------

st.sidebar.title("🚌 Chennai Transport Analyzer")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Dashboard",
        "Route Analytics",
        "Passenger Analytics",
        "Weather Analytics",
        "Delay Prediction",
        "Risk Monitoring",
        "Smart Insights",
        "Download Center"
    ]
)

# =====================================================
# EXECUTIVE DASHBOARD
# =====================================================

if page == "Executive Dashboard":

    st.title("🚌 Smart Chennai Public Transport Analyzer")

    cols = st.columns(5)

    for i, (_, row) in enumerate(kpis.head(5).iterrows()):
        cols[i].metric(
            str(row["Metric"]),
            str(row["Value"])
        )

    st.subheader("Delay Distribution")

    fig = px.histogram(
        dashboard,
        x="delay_minutes",
        title="Transport Delay Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Occupancy Distribution")

    fig = px.histogram(
        dashboard,
        x="occupancy_rate",
        title="Occupancy Rate Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# ROUTE ANALYTICS
# =====================================================

elif page == "Route Analytics":

    st.title("📊 Route Analytics")

    fig = px.bar(
        route_delay.head(20),
        x="route_id",
        y="delay_minutes",
        title="Top 20 Delayed Routes"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(
        route_util.head(20),
        x="route_id",
        y="trip_count",
        title="Top 20 Utilized Routes"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# PASSENGER ANALYTICS
# =====================================================

elif page == "Passenger Analytics":

    st.title("👥 Passenger Analytics")

    fig = px.bar(
        stop_volume.head(20),
        x="stop_id",
        y="passenger_count",
        title="Top Passenger Stops"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig = px.histogram(
        dashboard,
        x="passenger_count",
        title="Passenger Count Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# WEATHER ANALYTICS
# =====================================================

elif page == "Weather Analytics":

    st.title("🌦 Weather Analytics")

    fig = px.line(
        weather,
        x="date",
        y="temperature",
        title="Temperature Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(
        weather,
        x="date",
        y="humidity",
        title="Humidity Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(
        weather,
        x="date",
        y="rainfall",
        title="Rainfall Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# DELAY PREDICTION
# =====================================================

elif page == "Delay Prediction":

    st.title("🤖 AI Delay Prediction")

    hour = st.slider("Hour", 0, 23, 8)

    occupancy = st.slider(
        "Occupancy Rate",
        0.0,
        1.0,
        0.5
    )

    temp = st.slider(
        "Temperature",
        20.0,
        45.0,
        35.0
    )

    humidity = st.slider(
        "Humidity",
        0,
        100,
        70
    )

    input_df = pd.DataFrame({
        "hour": [hour],
        "occupancy_rate": [occupancy],
        "temperature": [temp],
        "humidity": [humidity]
    })

    pred = model.predict(input_df)[0]

    st.metric(
        "Predicted Delay (minutes)",
        round(float(pred), 2)
    )

# =====================================================
# RISK MONITORING
# =====================================================

elif page == "Risk Monitoring":

    st.title("🚨 Risk Monitoring")

    avg_delay = dashboard["delay_minutes"].mean()

    avg_occ = dashboard["occupancy_rate"].mean()

    risk = (
        avg_delay * 0.5
        + avg_occ * 100 * 0.3
    )

    if risk < 20:
        st.success("LOW RISK")

    elif risk < 50:
        st.warning("MEDIUM RISK")

    else:
        st.error("HIGH RISK")

    st.metric(
        "Risk Score",
        round(float(risk), 2)
    )

# =====================================================
# SMART INSIGHTS
# =====================================================

elif page == "Smart Insights":

    st.title("📈 Smart Insights")

    st.info(
        f"Route {route_delay.iloc[0]['route_id']} has the highest delay."
    )

    st.info(
        f"Route {route_util.iloc[0]['route_id']} has the highest utilization."
    )

    st.info(
        f"Average delay across network is {dashboard['delay_minutes'].mean():.2f} minutes."
    )

    st.info(
        f"Average occupancy rate is {dashboard['occupancy_rate'].mean()*100:.1f}%."
    )

# =====================================================
# DOWNLOAD CENTER
# =====================================================

elif page == "Download Center":

    st.title("📥 Download Reports")

    st.download_button(
        "Download Dashboard Data",
        dashboard.to_csv(index=False),
        "dashboard_data.csv"
    )

    st.download_button(
        "Download Route Delay Analysis",
        route_delay.to_csv(index=False),
        "route_delay_analysis.csv"
    )

    st.download_button(
        "Download Route Utilization",
        route_util.to_csv(index=False),
        "route_utilization.csv"
    )

    st.download_button(
        "Download Passenger Volume Data",
        stop_volume.to_csv(index=False),
        "stop_passenger_volume.csv"
    )
