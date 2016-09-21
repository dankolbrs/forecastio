from nose.tools import assert_is_not_none
from mock import patch

from lib.forecastio import ForecastIO


class TestForecast(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch('lib.forecastio.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_data_return(self):
        data = {
            "currently": {
                "data": "some stuff"
            }
        }
        self.mock_get.return_value.json.return_value = data
        test_forecast = ForecastIO('fake', 'fake', 'fake')
        assert_is_not_none(test_forecast.get_current())
