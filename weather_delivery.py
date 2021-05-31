import argparse
import requests

def argumentsParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--api_key', help="set API_KEY from the OPENWEATHER_API_KEY from the openweathermap.org")
    parser.add_argument('--city_name', help="set CITY_NAME from the CITY_NAME from the openweathermap.org")
    return parser


if __name__ == '__main__':
    parser = argumentsParser()
    args = parser.parse_args()
    # parameters for request
    API_KEY=format(args.api_key)
    CITY_NAME=format(args.city_name)
    LANG = "en"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + CITY_NAME + "&lang=" + LANG + "&appid=" + API_KEY
    if args.api_key and args.city_name:
        # HTTP request
        response = requests.get(URL)
        # che
        if response.status_code == 200:
            # getting data in the json format
            data = response.json()
            # getting the main and weather data
            main = data['main']
            weather = data['weather']
            # getting temperature
            temperature = main['temp']
            # getting the humidity
            humidity = main['humidity']
            # getting the pressure
            pressure = main['pressure']
            # getting the description
            description = weather[0]['description']
            # weather print info
            print("Source: openweathermap")
            print("City: {}".format(CITY_NAME))
            print("Description: {}".format(description))
            print("Temperature: {}".format(temperature))
            print("Humidity: {}".format(humidity))
            print("Pressure: {}".format(pressure))

        else:
            print("Mistakes in the HTTP request")
    else:
        print("Please input none data API_KEY = {} and CITY_NAME = {}!".format(args.api_key,args.city_name))
