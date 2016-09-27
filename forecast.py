#! /usr/bin/env python
from lib.forecastio import ForecastIO
from lib.influxdbwrap import InfluxDBWrapper
import configargparse
import os

p = configargparse.ArgParser(default_config_files=[
    str(os.path.dirname(__file__)) + './config.ini'])
p.add('-c', "--config", is_config_file=True, help="Config file path")
p.add("-a", "--apikey", required=True, help="ForecastIO apikey")
p.add("-t", "--lat", required=True, help="Latitude for weather forecast")
p.add("-n", "--lon", required=True, help="Longitude for weather forecast")
p.add("-o", "--host", required=False, help="Influxdb host")
p.add("-p", "--port", required=False, help="Influxdb port")
p.add("-u", "--username", required=False, help="Influxdb username")
p.add("-i", "--password", required=False, help="Influxdb password")
p.add("-d", "--database", required=False, help="Influxdb database")


options = p.parse_args()

forecast = ForecastIO(options.apikey, options.lat, options.lon)
influx_db_wrap = InfluxDBWrapper(options.host,
                                 options.port, options.username,
                                 options.password, options.database)

current = forecast.get_current()
influx_db_wrap.insert_current(current)
