import requests

API_ENDPOINT = "https://api.sunrise-sunset.org/json"





response = requests.get(url=API_ENDPOINT)
response.raise_for_status()
print(response.json())



"""

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
print(response.raise_for_status())
data = response.json()
print(data)

iss_position_data = response.json()["iss_position"]
print(iss_position_data)

iss_latitude_data = response.json()["iss_position"]["latitude"]
iss_longitude_data = response.json()["iss_position"]["longitude"]

iss_latitude_longitude_position = (iss_latitude_data, iss_longitude_data)
print(iss_latitude_longitude_position)
parameters = {
    "lat":
    "lng":
}

"""