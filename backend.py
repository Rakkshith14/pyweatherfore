import requests

APIkey = "43fb71923c688177c72e374c4401aae7"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(url)
    data = response.json()
    filter_data= data["list"]
    nr_values = 8 * forecast_days
    filter_data = filter_data[:nr_values]

    return filter_data

if __name__=="__main__":
    print(get_data(place = "Mumbai", forecast_days=3))
