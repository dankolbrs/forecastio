from influxdb import InfluxDBClient
import time


class InfluxDBWrapper(object):
    def __init__(self,
                 host,
                 port,
                 username,
                 password,
                 database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    def insert_current(self, current):
        self.client = InfluxDBClient(self.host,
                                     self.port,
                                     self.username,
                                     self.password,
                                     self.database)
        self.current = current
        self.time = time.gmtime(self.current["time"])
        self.time_conv = time.strftime("%Y-%m-%dT%H:%M:%SZ", self.time)
        # self.client.drop_database(self.database)
        # self.client.create_database(self.database)
        # print json_body
        json_body = [{
            "measurement": "forecastio",
            "tags": {
                "host": "forecastio"
            },
            "fields": {
                "temperature": float(self.current["temperature"]),
                "visibility": float(self.current["visibility"]),
                "summary": self.current["summary"],
                "apparentTemperature": float(
                    self.current["apparentTemperature"]),
                "pressure": float(self.current["pressure"]),
                "windSpeed": float(self.current["windSpeed"]),
                "windBearing": float(self.current["windBearing"]),
                "precipIntensity": float(self.current["precipIntensity"]),
                "precipPossibility": float(self.current["precipProbability"]),
                "humidity": float(self.current["humidity"]),
                "nearestStormDistance": self.current["nearestStormDistance"],
                "dewPoint": self.current["dewPoint"]
            },
            "time": self.time_conv
        }]
        # print json_body
        self.client.write_points(json_body)
