##Send ForecastIO data to Influxdb instance

To use:
* [Get a forecastio key](https://developer.forecast.io/)
* Stand up an [InfluxDB instance](https://www.influxdata.com/)
* Clone this repo
  * `git clone https://github.com/dankolbrs/forecastio.git`
* Install
  * `cd forecastio`
  * `python setup.py install`
* Copy config.example to config.ini, fill with your settings

## Running
`forecastio -c /path/to/config``

*Cron for best results*