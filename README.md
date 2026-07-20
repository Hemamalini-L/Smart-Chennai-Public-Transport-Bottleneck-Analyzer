# Smart-Chennai-Public-Transport-Bottleneck-Analyzer


## Project Overview

This project analyzes Chennai public transportation operations using GTFS transit data, weather analytics, and machine learning to identify transportation bottlenecks and improve mobility planning.

## Problem Statement

Public transportation systems often face challenges such as route delays, congestion, overcrowding, and inefficient scheduling. This project aims to identify bottlenecks in Chennai's public transport network and provide data-driven recommendations.

## Objectives

* Analyze route performance
* Identify congestion hotspots
* Study peak-hour traffic patterns
* Investigate weather impacts on transportation
* Predict route delays using machine learning

## Dataset

### Chennai Metro / MTC GTFS Data

Files Used:

* routes.txt
* stops.txt
* trips.txt
* stop_times.txt
* frequencies.txt

### Weather Data

Source: OpenWeatherMap API

Features:

* Temperature
* Humidity
* Rainfall
* Wind Speed

## Key Performance Indicators

* Total Routes
* Average Delay
* Passenger Volume
* Occupancy Rate
* On-Time Arrival Percentage
* Peak Congestion Hours
* Route Utilization
* High-Risk Routes

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Power BI
* Streamlit
* GitHub

## Dashboard Pages

### Executive Dashboard
<img width="1201" height="711" alt="Screenshot 2026-07-19 211334" src="https://github.com/user-attachments/assets/62c952a0-cb5f-47a3-88bf-8de3348794fb" />


* Route Statistics
* Delay Overview
* Passenger Volume

### Route Analytics
<img width="1195" height="707" alt="Screenshot 2026-07-19 211418" src="https://github.com/user-attachments/assets/4f65b510-8d35-4a2e-9294-cc47eab6a4f2" />


* Route Utilization
* Delay Trends

### Congestion Analytics
<img width="1188" height="697" alt="Screenshot 2026-07-19 211443" src="https://github.com/user-attachments/assets/130b48ce-821a-4440-9b81-bd07cc58ea3c" />


* Peak Hour Analysis
* Station Activity

### Weather Analytics

* Weather vs Delay
* Rainfall Impact

### Predictive Analytics

* Delay Prediction
* Risk Assessment

## Machine Learning Model

Model: Random Forest Regressor

Prediction Target:

* Delay Minutes

Input Features:

* Hour
* Temperature
* Humidity
* Occupancy Rate
* Traffic Index

## Results

The system identifies bottleneck routes, congestion hotspots, and weather-related disruptions while providing predictive insights for transportation planning.

## Future Scope

* Live GPS Integration
* Real-Time Traffic API
* Passenger Demand Forecasting
* Smart Route Optimization
* AI-Based Scheduling System

## Author

Hemamalini L
B.Tech Artificial Intelligence and Data Science
Vivekanandha College of Technology for Women
