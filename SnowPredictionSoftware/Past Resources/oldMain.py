'''
Authors: Frank Vanris, Conrad Nark, Stefana Ciustea
Date: 4/9/2024
Desc: This is the main file where everything will project the given information for Snow Prediction.
'''
import argparse
from datetime import datetime, timedelta
import time

import numpy as np
import pandas as pd

from CurrentWeatherAveraging import CurrentHourlyWeatherChange

from WeatherAPI import weatherAPI
from prediction_code import getPrediction


#Unit Testing will occur beyond this line as well as our main method compiling everything.

def main():

    avgD = CurrentHourlyWeatherChange()

    #my average dataframe
    avgData = avgD.makeDF()

    #args for the main we can pass in if we want to obtain the data at any given time
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--Now", help="obtaining data now")
    args = parser.parse_args()

    apiRunning(avgD, avgData, args)



def datetime_to_float(d):
    return d.timestamp()

def update_avg_data(avgD, avgData, newDataFrame):
    avgData['mintempF'] = avgD.determineMin(avgData['mintempF'], newDataFrame['mintempF'])
    avgData['maxtempF'] = avgD.determineMax(avgData['maxtempF'], newDataFrame['maxtempF'])
    avgData['avgtempF'] = avgD.averagingHourlyTemp(avgData['avgtempF'], newDataFrame['avgtempF'])
    avgData['totalprecipIn'] = avgD.sumPrecip(avgData['totalprecipIn'], newDataFrame['totalprecipIn'])

def apiRunning(avgD, avgData, args):
    # time interval for weather API
    while True:
        if not args.Now:
            # (sleep for 1 hour)
            current_time = datetime.today()
            time_until_next_hour = 3600 - current_time.minute * 60 - current_time.second
            print("current time: " + str(current_time))
            print("waiting till program reaches an hour for data retrieval...")

            retrievalTime = current_time + timedelta(seconds=time_until_next_hour)
            print("retrieval time: " + str(retrievalTime))
            time.sleep(time_until_next_hour)

        current_time = datetime.today()
        print("starting API Time: " + str(current_time))
        # api call
        weatherAPI()
        avgData = obtainingCurrentHourlyData(avgD, avgData)
        thePredictionsofAPI(avgD, avgData)
        # bailout if needed
        if args.Now:
            return

def obtainingCurrentHourlyData(avgD, avgData):
    # retrieving and storing data

    currentData = avgD.getCurrentDF()
    hourlyData = avgD.getHourlyDF()

    # getting current time and hourly time predictions
    currentData['datetime'] = pd.to_datetime(currentData['datetime'])
    hourlyData['datetime'] = pd.to_datetime(hourlyData['datetime'])

    #changing the hour to the current hour
    avgD.hour = currentData['datetime'].dt.hour

    # current time information
    currentTime = currentData['datetime'].iloc[0]

    # filter data between dates
    filteredData = hourlyData[(hourlyData['datetime'].dt.year == currentTime.year) &
                              (hourlyData['datetime'].dt.month == currentTime.month) &
                              (hourlyData['datetime'].dt.day == currentTime.day) &
                              (hourlyData['datetime'].dt.hour != currentTime.hour)]

    # Create a new DataFrame for hourly data predictions
    updatedHourlyData = hourlyData[hourlyData['datetime'].isin(filteredData['datetime'])]

    # hourly data predictions
    # Creating a new DataFrame with the required structure
    newHourlyDataFrame = pd.DataFrame({
        'mintempF': [np.rint((updatedHourlyData['temp'].min()) * (9 / 5)) + 32],
        'maxtempF': [np.rint((updatedHourlyData['temp'].max()) * (9 / 5)) + 32],
        'avgtempF': [np.rint((updatedHourlyData['temp'].mean()) * (9 / 5)) + 32],
        'totalprecipIn': [(updatedHourlyData['precip'].sum()) / 25.4]
    }).round({'totalprecipIn': 1})

    # rounding the numbers
    print("New Hourly DataFrame: \n" + str(newHourlyDataFrame))

    # currentData predictions
    newCurrentDataFrame = avgD.makeDF()
    newCurrentDataFrame['mintempF'] = (currentData['temp'] * (9 / 5)) + 32
    newCurrentDataFrame['maxtempF'] = (currentData['temp'] * (9 / 5)) + 32
    newCurrentDataFrame['avgtempF'] = (currentData['temp'] * (9 / 5)) + 32
    newCurrentDataFrame['totalprecipIn'] = currentData['precip'] / 25.4

    print("New Current Temp: \n" + str(newCurrentDataFrame))

    # condition to see if we have the avgDataframe with data or not OR we have reached the end of the day
    if avgData.empty or avgD.getHour() == 23:
        if not avgData.empty:
            avgD.storeDaysData(avgData)
            avgD = CurrentHourlyWeatherChange()  # Resetting for the new day
        else:

            # inserting current average
            avgData = newCurrentDataFrame
            update_avg_data(avgD, avgData, newHourlyDataFrame)

    else:
        # averaging with current first
        update_avg_data(avgD, avgData, newCurrentDataFrame)
        update_avg_data(avgD, avgData, newHourlyDataFrame)

    return avgData


def thePredictionsofAPI(avgD, avgData):
    # create the prediction
    prediction = getPrediction(avgData)

    print("Averaged Data with hourly and current: \n" + str(avgData))
    print("snowfall in inches for the 24 hour period is: " + str(prediction) + "in")
    avgD.iterateHour()

if __name__ == "__main__":
    main()