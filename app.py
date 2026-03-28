import streamlit as st
import pandas as pd
import math
import os
from geopy.geocoders import Nominatim

st.set_page_config(page_title="Hospital Finder", layout="wide")
# st.sidebar.image("logo.jpg", use_container_width=True)


st.markdown("""
    <style>
    .main {
        # background: linear-gradient(to right, #e3f2fd, #ffffff);
        background: linear-gradient(red, blue);
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #0d47a1;
        text-align: center;
    }
    .subtitle {
        font-size: 18px;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        padding: 20px;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🏥 AI Emergency Response Optimization System</div>', unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Find nearest hospitals instantly based on your location, available beds, and specialist doctors.
This system helps optimize emergency response by providing fast and intelligent hospital recommendations.
</div>
""", unsafe_allow_html=True)

image = st.image("logo.jpg")

if not os.path.exists("./Dataset/hospitals.csv"):
    hospitals_data = pd.DataFrame({
        "hospital_name": [
            "Apollo Hospital", "Yashoda Hospital", "Care Hospital",
            "KIMS Hospital", "AIG Hospital", "Sunshine Hospital"
        ],
        "address": [
            "Jubilee Hills", "Somajiguda", "Banjara Hills",
            "Secunderabad", "Gachibowli", "SR Nagar"
        ],
        "latitude": [17.4239, 17.4260, 17.4126, 17.4399, 17.4401, 17.4415],
        "longitude": [78.4738, 78.4560, 78.4482, 78.4983, 78.3489, 78.4950],
        "available_beds": [20, 15, 10, 25, 18, 12],
        "available_doctors": [10, 8, 6, 12, 9, 7],
        "specialist": [
            "Cardiologist", "Neurologist", "Orthopedic",
            "General", "Multi-specialist", "Emergency"
        ]
    })
    hospitals_data.to_csv("./Dataset/hospitals.csv", index=False)

hospitals_df = pd.read_csv("./Dataset/hospitals.csv")

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat/2)**2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon/2)**2)
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))


st.sidebar.header("🔍 Search Options")

geolocator = Nominatim(user_agent="hospital_finder")

location_text = st.sidebar.selectbox(
    "Select Location",["Select Location"] +
    [
        "Jubilee Hills", "Somajiguda", "Banjara Hills",
        "Secunderabad", "Gachibowli", "Paradise"
    ]
)

user_lat, user_lon = None, None

if location_text:
    location = geolocator.geocode(location_text)
    if location:
        user_lat = location.latitude
        user_lon = location.longitude
        st.sidebar.success("📍 Location detected")
    else:
        st.sidebar.error("Location not found")

specialties = st.sidebar.multiselect(
    "Select Specialist",
    hospitals_df['specialist'].unique()
)

radius = st.sidebar.slider("Search Radius (km)", 1, 50, 10)

search_btn = st.sidebar.button("🚀 Search Hospitals")

if search_btn and user_lat and user_lon:
    
    image.empty()
    
    hospitals_df['distance_km'] = hospitals_df.apply(
        lambda row: calculate_distance(user_lat, user_lon, row['latitude'], row['longitude']),
        axis=1
    )

    filtered_df = hospitals_df[hospitals_df['distance_km'] <= radius]

    if specialties:
        filtered_df = filtered_df[filtered_df['specialist'].isin(specialties)]

    nearest = filtered_df.sort_values(by='distance_km').head(5)

    st.subheader("🏥 Nearby Hospitals")

    if not nearest.empty:
        for _, row in nearest.iterrows():
            st.markdown(f"""
            <div class="card">
                <h4>🏥 {row['hospital_name']}</h4>
                <p>📍 {row['address']}</p>
                <p>📏 Distance: {row['distance_km']:.2f} km</p>
                <p>🛏 Beds Available: {row['available_beds']}</p>
                <p>👨‍⚕️ Doctors: {row['available_doctors']}</p>
                <p>🩺 Specialist: {row['specialist']}</p>
            </div>
            """, unsafe_allow_html=True)

        st.dataframe(nearest, use_container_width=True)

    else:
        st.warning("No hospitals found within selected radius")

elif search_btn:
    st.error("Please select a valid location")