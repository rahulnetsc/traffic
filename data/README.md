# 📂 data/ 

This module handles all tasks related to data acquisition and preprocessing for the Air Quality Index (AQI) dashboard.

---

## ⏱️ Responsibilities

- Fetch raw Air Quality Index (AQI) from external sources (e.g. OpenAQ API)
- The API data needs to be cleaned and normalized for downstream functions
- Define core configurations like target city and pollutants

---

## 📁 Overview 

### 🗃️ `interface.py`
- Implements OpenAQClient class for communicating with the OpenAQ API 
- Fetches real time and historical AQI data for a given city 
- Responsible for handling real time requests, request errors and standardizing output format

### 🗃️ `clean.py` 
- Processes raw AQI data JSON data returned by the API
- Extracts key pollutants (eg. PM2.5, PM10) cleans timestamps, units and formats 
- Returns a cleaned structure (eg. Pandas dataframe or csv) for visualization and modeling

### 🗃️ `config.py` 
- Defines key project constants such as city name, pollutant types, and base APi URLs
- Optionally loads environment variables from `.env` using `python-dotenv`

---

## Future additions
- `scheduler.py`: Automate periodic data collection
- `storage.py`: Manage saving to CSV or database 

## 🎈 Notes
- This module is importable via `from data import interface, config, clean`
- `.env` file should not be committed and must contain any required info if API keys are used later


