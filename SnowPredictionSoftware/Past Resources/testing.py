'''
By: Frank Vanris
Date: 6/2/2024
Desc: For testing purposes in creating predictions out of current data
'''
import pandas as pd
import numpy as np

from prediction_code import getPrediction

currentData = pd.read_csv("../RelevantData/Current_Hourly_Data/snoqualmie_pass_current.csv")

specifiedCurrentData = ['datetime', 'temp', 'precip']

currentData = currentData[specifiedCurrentData]

min_temp = currentData['temp'].min()
currentData['mintempF'] = min_temp

max_temp = currentData['temp'].max()
currentData['maxtempF'] = max_temp





specifiedCurrentData = ['mintempF', 'temp', 'maxtempF', 'precip']

currentData = currentData[specifiedCurrentData]

currentData['temp'] = ((9/5) * currentData['temp']) + 32
currentData['mintempF'] = ((9/5) * currentData['mintempF']) + 32
currentData['maxtempF'] = ((9/5) * currentData['maxtempF']) + 32




currentData['avgtempF'] = currentData['temp']
currentData['totalprecipIn'] = currentData['precip']


specifiedCurrentData = ['maxtempF', 'mintempF', 'avgtempF', 'totalprecipIn']

currentData = currentData[specifiedCurrentData]


print(currentData.head())

df = pd.read_csv('../RelevantData/HistoricalRelevantData/kNNReadyScaledFeatures.csv')
df = df.drop(df.columns[0], axis=1)
print(df.head())
print()
#testing snow in inches
print(getPrediction(currentData))
#CurrentData averages and sums with pastData

#current with past becomes averageData

#AverageData will become pastData after an hour


