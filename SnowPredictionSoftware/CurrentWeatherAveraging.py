'''
By: Frank Vanris
Date: 5/26/2024
Desc: Obtaining the current data based on the hours and averaging them with the given data
'''

import pandas as pd
import numpy as np


class CurrentHourlyWeatherChange:

    def __init__(self):
        self.hour = 1

    def makeDF(self):
        return pd.DataFrame(columns=['mintempF', 'maxtempF', 'avgtempF', 'totalprecipIn'])

    def getHour(self):
        return self.hour

    def iterateHour(self):
        self.hour += 1

    def getCurrentDF(self):
        return pd.read_csv('RelevantData/snoqualmie_pass_current.csv')

    def getHourlyDF(self):
        return pd.read_csv('RelevantData/snoqualmie_pass_hourly.csv')

    def averagingCurrentTemp(self, avgHourTemp, newHourTemp):
        hour = self.getHour()
        newAvgTemp = (avgHourTemp * (hour - 1) + newHourTemp) / hour
        return newAvgTemp

    def averagingHourlyTemp(self, avgHourTemp, newHourlyTemp):
        hour = 2
        avgHourTemp = (avgHourTemp + newHourlyTemp) / 2
        return avgHourTemp

    def determineMin(self, minHourTemp, newHourTemp):
        return minHourTemp.combine(newHourTemp, min)

    def determineMax(self, maxHourTemp, newHourTemp):
        return maxHourTemp.combine(newHourTemp, max)

    def sumPrecip(self, currentHourPrecip, newHourPrecip):
        currentHourPrecip += newHourPrecip
        return currentHourPrecip

    def storeDaysData(self, df):
        dataForModel = pd.read_csv("dataToBeAddedToModel.csv")
        df['24HourSnow'] = np.nan
        dataForModel = dataForModel.append(df, ignore_index=True)

    #def storeSnow(df):
    #   snowDataForTarget = pd.read_csv("snowpred.csv")



