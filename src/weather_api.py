import requests

latitude = 35.6895
longitude = 139.6917

location_name = "Mainz, Germany"

print(
    "Der Wohnort ist "
    + location_name
    + " mit den Koordinaten: "
    + str(latitude)
    + ", "
    + str(longitude)
)


url = "https://api.open-meteo.com/v1/forecast"
querystring = {
    "latitude": latitude,
    "longitude": longitude,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode",
}
response = requests.get(url, params=querystring)
print(response)


data = response.json()
# print(data)

for i in range(len(data["daily"]["time"])):
    print(
        "Um "
        + str(data["daily"]["time"][i])
        + " Uhr "
        + str(data["daily"]["temperature_2m_max"][i])
        + "°C"
    )


historical_url = "https://archive-api.open-meteo.com/v1/archive"

historical_querystring = {
    "latitude": latitude,
    "longitude": longitude,
    "start_date": "2019-03-08",
    "end_date": "2019-03-08",
    "daily": "temperature_2m_mean",
}

historical_response = requests.get(params=historical_querystring, url=historical_url)

historical_data = historical_response.json()

# print(historical_data)

print(
    "Die Temperatur am "
    + historical_data["daily"]["time"][0]
    + " war "
    + str(historical_data["daily"]["temperature_2m_mean"][0])
    + "°C"
)
