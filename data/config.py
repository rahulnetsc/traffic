"""
Configuration file for AQI Dashboard.
Loads API keys, city, pollutant types, and endpoint URLs.
"""

import os
from dotenv import load_dotenv

load_dotenv()

OPENAQ_API_KEY = os.getenv("OPENAQ_API_KEY")

if not OPENAQ_API_KEY:
    raise ValueError("Missing OPENAQ_API_KEY. Did you forget to set it in your .env?")

API_HEADERS = {
    "x-api-key": OPENAQ_API_KEY
}

CITY = "Bangalore"
# Approximate bounding box for Bangalore (min_lng, min_lat, max_lng, max_lat)
BANGALORE_BBOX = (77.45, 12.8, 77.75, 13.2)


POLLUTANTS = ["pm25", "pm10", "no2"]

# API endpoints
OPENAQ_BASE_URL = "https://api.openaq.org/v3/latest"
OPENAQ_HISTORICAL_URL = "https://api.openaq.org/v3/measurements"
OPENAQ_LOCATIONS_URL = "https://api.openaq.org/v3/locations" 

SAVE_RAW_JSON = True   # Optionally save API response to disk
REQUEST_TIMEOUT = 10   # Seconds
