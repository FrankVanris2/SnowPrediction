import unittest

import numpy as np
import pandas as pd

'''
By: Frank Vanris
Date: 6/2/2024
Desc: Junit testing with python for my API Calling, AveragingWeatherCurrent class, and WeatherAPI func
'''

from CurrentWeatherAveraging import CurrentHourlyWeatherChange
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.avgD = CurrentHourlyWeatherChange()

    #Testing CurrentWeatherAveraging file
    def test_get_hour(self):
        hour = self.avgD.getHour()
        self.assertEqual(hour, 1)  # add assertion here

    def test_iterating_hour(self):
        self.avgD.iterateHour()
        hour = self.avgD.getHour()
        self.assertEqual(hour, 2)

    def test_averaging_current_temp(self):
        self.avgD.iterateHour()
        averaged_temp = 45
        new_hour_temp = 50
        new_averaged_temp = self.avgD.averagingCurrentTemp(averaged_temp, new_hour_temp)
        self.assertEqual(new_averaged_temp, 47.5)

    def test_averaging_hourly_temp(self):
        averaged_hourly_temp = 48.6
        new_hour_temp = 52
        new_averaged_hourly_temp = self.avgD.averagingHourlyTemp(averaged_hourly_temp, new_hour_temp)
        self.assertAlmostEqual(new_averaged_hourly_temp, 48.74782608)

    def test_min_temp(self):
        hourly_data = {
            'tempMin': ['48.5']
        }

        current_data = {
            'tempMin': ['23.4']
        }

        hourly_data_df = pd.DataFrame(hourly_data)
        current_data_df = pd.DataFrame(current_data)

        min_temp_hourlyDataFrame = pd.DataFrame([])
        hourly_data_df['tempMin'] = self.avgD.determineMin(hourly_data_df['tempMin'], current_data_df['tempMin'])
        self.assertEqual(hourly_data_df['tempMin'].item(), current_data_df['tempMin'].item())

    def test_max_temp(self):
        hourly_data = {
            'tempMax': ['48.5']
        }

        current_data = {
            'tempMax': ['60.4']
        }

        hourly_data_df = pd.DataFrame(hourly_data)
        current_data_df = pd.DataFrame(current_data)

        min_temp_hourlyDataFrame = pd.DataFrame([])
        hourly_data_df['tempMax'] = self.avgD.determineMax(hourly_data_df['tempMax'], current_data_df['tempMax'])
        self.assertEqual(hourly_data_df['tempMax'].item(), current_data_df['tempMax'].item())

    def test_precip_sum(self):
        first_precip = 0.4
        second_precip = 0.5
        summed_precip = self.avgD.sumPrecip(first_precip, second_precip)
        self.assertEqual(summed_precip, 0.9)

    def test_make_df(self):
        newDF = self.avgD.makeDF()
        self.assertTrue((newDF.columns == ['mintempF', 'maxtempF', 'avgtempF', 'totalprecipIn']).all())


if __name__ == '__main__':
    unittest.main()
