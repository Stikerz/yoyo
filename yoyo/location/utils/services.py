import statistics
from datetime import datetime, timedelta

import requests

from yoyo.settings import WEATHER_KEY


def get_weather_history(payload):
    try:
        response = requests.get(
            "http://api.weatherapi.com/v1/history.json", params=payload
        )
        data = response.json()
        if len(data) == 2:
            forecast_day = data["forecast"]["forecastday"][0]["day"]
            info = {
                "average": forecast_day["avgtemp_c"],
                "minimum": forecast_day["mintemp_c"],
                "maximum": forecast_day["maxtemp_c"],
            }
            return info
        else:
            raise Exception(f"Error retrieving weather:{payload['q']} City")

    except requests.exceptions.ConnectionError as errc:
        raise Exception(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        raise Exception(f"Timeout Error: {errt}")
    except requests.exceptions.HTTPError as errh:
        raise Exception(f"Http Error: {errh}")
    except requests.exceptions.RequestException as err:
        raise Exception(f"Error: {err}")


def get_weather_api_key():

    if WEATHER_KEY is None:
        raise Exception(
            f"Error retrieving weather key from env variable 'WEATHER_KEY'  "
            f"please make sure key is set"
        )

    return WEATHER_KEY


def get_city_weather_info(city, days):

    dates = [datetime.today().strftime("%Y-%m-%d")]
    maximum = []
    minimum = []
    average = []

    for day in range(1, int(days)):
        d = datetime.today() - timedelta(days=day)
        dates.append(d.strftime("%Y-%m-%d"))

    payload = {"key": get_weather_api_key(), "q": city}

    for date in dates:
        payload["dt"] = date
        data = get_weather_history(payload)
        maximum.append(data["maximum"])
        minimum.append(data["minimum"])
        average.append(data["average"])

    info = {
        "median": round(statistics.median(average), 2),
        "average": round(statistics.mean(average), 2),
        "minimum": round(min(minimum), 2),
        "maximum": round(max(maximum), 2),
    }

    return info
