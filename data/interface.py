import requests
from config import OPENAQ_BASE_URL, OPENAQ_HISTORICAL_URL, OPENAQ_API_KEY,OPENAQ_LOCATIONS_URL,\
                    API_HEADERS, REQUEST_TIMEOUT, POLLUTANTS, CITY, BANGALORE_BBOX
from tqdm import tqdm

class OpenAQClient:

    def __init__(self):
        
        self.base_url = OPENAQ_BASE_URL
        self.hist_url = OPENAQ_HISTORICAL_URL
        self.locations_url = OPENAQ_LOCATIONS_URL

    def get_nearby_locations(self, limit=5, bbox= BANGALORE_BBOX, ):
        # params = {
        #     "bbox": ",".join([str(coord) for coord in bbox]),  # Convert tuple to string
        #     # "limit": limit,
        #     # "country": "IN",
        # }
        params = {
                "country": "IN",
                "limit": 5
            }

        try:
            self.base_url = "https://api.openaq.org/v3/locations"

            print(f"self.base_url = {self.base_url}\n")

            response = requests.get(
                # url=self.locations_url,
                url=self.base_url,
                params=params,
                headers=API_HEADERS,
                timeout=REQUEST_TIMEOUT
                )
            response.raise_for_status()
            response = response.json()
            return response.get("results", [])
        except Exception as e:
            print(f"Failed to fetch nearby locations: {e}")
            return []
        
    def get_latest_aqi(self,):
        # Query using API

        try:
            client_response = self.get_nearby_locations(limit= 5)
            print("client response")
            for i,client_data in enumerate(client_response):
                print(f"\ni: {i}")
                print(client_data)
            
        #     for loc in tqdm(client_response,desc= "ID"):

        #         location_id = loc["id"]
        #         # print(f"\nTrying location: {loc['name']} (ID: {location_id})")

        #         params = {"location_id": location_id}
        #         response = requests.get(
        #             url=self.base_url,
        #             params=params,
        #             headers=API_HEADERS,
        #             timeout=REQUEST_TIMEOUT
        #         )

        #         # print(f"→ URL: {response.url}")
        #         # print(f"→ Status: {response.status_code}")

        #         if response.status_code == 200:
        #             print("✅ Found a location with recent data!")
        #             from pprint import pprint
        #             pprint(response.json())
        #             return


        except Exception as e:
            print(f"Request received exception {e}")

    def get_historical_aqi(self, time):
        pass

    def print_response(self, client_response):
        
        from pprint import pprint

        print("Client response:")

        for i, loc in enumerate(client_response):
            print(f"\nLocation {i+1}: {loc['name']}")
            print(f"Coordinates: {loc['coordinates']}")
            print(f"Last Measurement: {loc.get('datetimeLast', {}).get('local', 'N/A')}")
            print("Pollutants measured:")
            for sensor in loc.get("sensors", []):
                print(f"  - {sensor['parameter']['displayName']} ({sensor['parameter']['name']})")

client = OpenAQClient()
client_response = client.get_nearby_locations()

if client_response:
    # from pprint import pprint
    # pprint(client_response.json())
    print(client_response)
# client_response = client.get_latest_aqi()




