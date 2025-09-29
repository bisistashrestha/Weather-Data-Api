# 🌦️ Flask Weather Data API  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python) 
![Flask](https://img.shields.io/badge/Flask-API-green?logo=flask) 
![License](https://img.shields.io/badge/License-MIT-yellow.svg) 
![Data](https://img.shields.io/badge/Weather-Data-orange)  

A simple Flask-based API that serves historical weather data (temperature readings) from the `weather_data` dataset. The project provides endpoints to query temperature by station, date, year, or fetch all available records for a station.  

---

## 📌 Features
- Home route displaying station list **with API usage instructions**.  
- API to get **temperature for a specific station & date**.  
- API to get **all weather data for a station**.  
- API to get **yearly weather data for a station**.  

---

## 🛠️ Tech Stack
- **Python**  
- **Flask** (for API routing & rendering)  
- **Pandas** (for CSV data handling)  
- **HTML (Jinja Templates)** for homepage  

---

## 📂 Project Structure
```bash
.
│── weather_data/
│   ├── stations.txt        #Station metadata
│   ├── TG_STAID000001.txt  #Temperature data files
│   ├── TG_STAID000002.txt
│   └── ...
│── templates/
│   └── home.html           #Homepage template with API Usage
│── main.py
│── README.md
│── LICENSE
│── Requirements.txt
```

---

## 🚀 Installation & Setup

1. **Clone the repository**  
```bash
git clone <your-repo-url>
cd <project-folder>
```

2.**Install dependencies**
```bash 
pip install -r Requirements.txt
```

3. **Run the App**
```bash
python main.py
```

4. **Open Your Browser at:**
```
http://127.0.0.1:5000/
```

---

## 📊 API Endpoints

**1️⃣ Home (Station list + API docs)**
```
GET /
```
Displays usage instructions and a list of available weather stations.

**2️⃣ Get temperature by station & date**
```
GET /api/v1/<station>/<date>
```
Example:
```
/api/v1/10/19980830
```
Response:
```
{
  "station": "10",
  "date": "19980830",
  "temperature": 21.5
}
```

**3️⃣ Get all data for a station**
```
GET /api/v1/<station>
```
Example:
```
/api/v1/10
```

**4️⃣ Get yearly data for a station**
```
GET /api/v1/yearly/<station>/<year>
```
Example:
```
/api/v1/yearly/10/1998
```

---

## 📌 Notes
- Temperatures are stored in tenths of °C (e.g., 215 → 21.5°C).
- Missing values are represented as -9999 and converted to NaN by Pandas.
- Station IDs are zero-padded to 6 digits (e.g., 10 → 000010).

---

## ✨ Future Improvements
- Add endpoints for monthly averages.
- Provide CSV/JSON download options.
- Build a frontend dashboard for data visualization.

---

## 📜 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

