# AI-Emergency-Response-Optimization-System
Emergency response systems often face critical delays due to lack of coordination between ambulance routing, hospital availability, and real-time patient demand. In many cases, ambulances transport patients to the nearest hospital without knowing whether beds or medical staff are available, resulting in delays, overcrowding, and compromised patient
The **AI Emergency Hospital Finder** is a Streamlit-based web application that helps users quickly locate nearby hospitals based on their location, available beds, and specialist doctors.
It is designed to assist in emergency situations by providing fast, filtered, and accurate hospital recommendations.

---

## 🚀 Features

* 📍 Location-based hospital search (City/Area selection)
* 📏 Distance calculation using geospatial logic (Haversine formula)
* 🛏 Filter hospitals based on available beds
* 👨‍⚕️ Filter by specialist doctors
* 🎯 Top nearest hospitals recommendation
* 🎨 Clean and professional UI (cards layout + sidebar filters)
* ⚡ Fast and interactive user experience

---

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python
* **Libraries Used:**

  * pandas
  * geopy
  * math
  * streamlit
* **Data Storage:** CSV (custom dataset)

---

## 📂 Project Structure

```
project/
│── app.py
│── logo.png
│── Dataset/
│   └── hospitals.csv
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Pyyus/AI-Emergency-Response-Optimization-System.git
cd AI-Emergency-Response-Optimization-System
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install streamlit pandas geopy
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots


<img width="1918" height="1079" alt="image" src="https://github.com/user-attachments/assets/ea47a4d5-7689-473a-8552-7c2baea1df6e" />

---

## 🧠 How It Works

1. User selects a location from the sidebar
2. System converts location into latitude & longitude
3. Distance is calculated between user and hospitals
4. Filters (radius & specialization) are applied
5. Top nearest hospitals are displayed

---

## 🎯 Use Cases

* Emergency hospital search
* Healthcare accessibility tools
* Smart city applications
* AI-based resource optimization systems

---

## 🚀 Future Enhancements

* 🗺️ Map integration (PyDeck / Google Maps)
* 📍 Auto-detect user location (GPS)
* 🚑 Ambulance optimization system
* ⏱ Travel time estimation
* 📊 Analytics dashboard

---

## 👨‍💻 Author

**Piyush Gupta**
B.Tech CSE (2025)
Aspiring Data Analyst / Developer

---

## ⭐ Contribute

Feel free to fork this repository and improve the project!

---

## Live

https://aihospitalfinder.streamlit.app/
