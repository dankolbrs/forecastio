import requests


class ForecastIO(object):
    def __init__(self, apikey, lat, lon):
        # https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE
        self.url = "https://api.forecast.io/forecast/"
        self.apikey = apikey
        self.lat = lat
        self.lon = lon
        self._get_forecast()

    def test_forecast(self):
        # forecast_raw = open("~/Documents/forecastio.out").read()
        # forecast_json = json.loads(forecast_raw)
        # return forecast_raw
        pass

    def _get_forecast(self):
        self.forecast = ""
        # to be replaced with API call after testing
        weather_url = self.url + "%s/%s,%s" % (self.apikey,
                                               self.lat,
                                               self.lon)
        weather_req = requests.get(weather_url)
        self.forecast = weather_req.json()

    def get_current(self):
        return self.forecast["currently"]
