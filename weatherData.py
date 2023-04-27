# importing requests and json
import requests, json



def get_precipitation():
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast?"
    # City Name
    CITY = "Platteville"
    # API key
    API_KEY = "6d028003cc35a12dcf22c30e948c703b"
    # upadting the URL
    URL = FORECAST_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)

    # Checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        print(data)
        precipitation = []

        for forecast in data['list']:
            if 'rain' in forecast and '3h' in forecast['rain']:
                precipitation.append(forecast['rain']['3h'])
            else:
                precipitation.append(0)
        print(precipitation)

    else:
        # showing the error message
        print("Error in the HTTP request")

#get_precipitation()