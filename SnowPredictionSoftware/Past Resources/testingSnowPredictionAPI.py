'''
By: Frank Vanris
Date: 5/27/2024
Desc: This testing environment was meant to learn how to obtain past and current data and combine them with
averaging in order to obtain a prediciton
'''


import numpy as np
import pandas as pd

from CurrentWeatherAveraging import CurrentHourlyWeatherChange
from WeatherAPI import weatherAPI
from prediction_code import getPrediction

avgD = CurrentHourlyWeatherChange()

#my average dataframe
avgData = avgD.makeDF()

#api call
weatherAPI()

# retrieving and storing data

currentData = pd.read_csv("TestingFiles/january13Current.csv")

hourlyData = pd.read_csv("TestingFiles/january132024.csv")

# getting current time and hourly time predictions
currentData['datetime'] = pd.to_datetime(currentData['datetime'])
hourlyData['datetime'] = pd.to_datetime(hourlyData['datetime'])

avgD.hour = currentData['datetime'].dt.hour

#current time information
currentTime = currentData['datetime'].iloc[0]

print("currentTime Data: \n" + str(currentTime))

#filter data between dates
filteredData = hourlyData[(hourlyData['datetime'].dt.year == currentTime.year) &
                          (hourlyData['datetime'].dt.month == currentTime.month) &
                          (hourlyData['datetime'].dt.day == currentTime.day) &
                          (hourlyData['datetime'].dt.hour < currentTime.hour)]


#Create a new DataFrame for hourly data predictions
updatedHourlyData = hourlyData[hourlyData['datetime'].isin(filteredData['datetime'])]
updatedHourlyData = pd.DataFrame(updatedHourlyData)

updatedHourlyData = updatedHourlyData._append(currentData, ignore_index=True)

#hourly data predictions
# Creating a new DataFrame with the required structure
newHourlyDataFrame = pd.DataFrame({
    'mintempF': [np.rint((updatedHourlyData['temp'].min()) * (9/5)) + 32],
    'maxtempF': [np.rint((updatedHourlyData['temp'].max()) * (9/5)) + 32],
    'avgtempF': [np.rint((updatedHourlyData['temp'].mean()) * (9/5)) + 32],
    'totalprecipIn': [(updatedHourlyData['precip'].sum()) / 25.4]
}).round({'totalprecipIn': 1})

print("update hourly data: \n" + str(updatedHourlyData['datetime']) + ", " + str(updatedHourlyData['temp']))
#rounding the numbers
print("New Hourly DataFrame: \n" + str(newHourlyDataFrame))



#condition to see if we have the avgDataframe with data or not OR we have reached the end of the day
if avgData.empty or avgD.getHour() == 23:
    if not avgData.empty:
        avgD.storeDaysData(avgData)
        avgD = CurrentHourlyWeatherChange() # Resetting for the new day
    else:

        #inserting current average
        avgData = newHourlyDataFrame

else:

    #averaging with current first
    avgData = newHourlyDataFrame

#create the prediction
prediction = getPrediction(avgData)

print("Averaged Data with hourly and current: \n" + str(avgData))
print("snowfall in inches for the 24 hour period is: " + str(prediction) + "in")
avgD.iterateHour()



