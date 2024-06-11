'''
Authors: Frank Vanris, Conrad Nark, Stefana Ciustea
Contributors of Main: Frank Vanris, Conrad Nark
Date: 4/9/2024
Desc: This is the main file where everything will project the given information for Snow Prediction.
'''
import argparse
import json
from datetime import datetime, timedelta
import time
from datetime import date

import numpy as np
import pandas as pd

from CurrentWeatherAveraging import CurrentHourlyWeatherChange

from WeatherAPI import weatherAPI
from prediction_code import getPrediction


#Unit Testing will occur beyond this line as well as our main method compiling everything.
todayPrediction = 5
def main():
    try:
        avgD = CurrentHourlyWeatherChange()

        #my average dataframe
        avgData = avgD.makeDF()

        #args for the main we can pass in if we want to obtain the data at any given time
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", "--Now", action='store_true',  help="obtaining data now")
        args = parser.parse_args()

        apiRunning(avgD, avgData, args)
    except Exception as e:
        print(f"an error occurred in the main function: {e}")


def datetime_to_float(d):
    return d.timestamp()

def update_avg_data(avgD, avgData, newDataFrame):
    avgData['mintempF'] = avgD.determineMin(avgData['mintempF'], newDataFrame['mintempF'])
    avgData['maxtempF'] = avgD.determineMax(avgData['maxtempF'], newDataFrame['maxtempF'])
    avgData['avgtempF'] = avgD.averagingHourlyTemp(avgData['avgtempF'], newDataFrame['avgtempF'])
    avgData['totalprecipIn'] = avgD.sumPrecip(avgData['totalprecipIn'], newDataFrame['totalprecipIn'])

def apiRunning(avgD, avgData, args):
    # time interval for weather API
    try:
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

            print("AveragedData Checking:\n" + str(avgData))

            thePredictionsofAPI(avgD, avgData)
            # bailout if needed
            if args.Now:
                return
    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting...")
    except Exception as e:
        print(f"An error occurred in apiRunning: {e}")

def obtainingCurrentHourlyData(avgD, avgData):
    global todayPrediction
    # retrieving and storing data
    try:
        currentData = avgD.getCurrentDF()
        hourlyData = avgD.getHourlyDF()

        # getting current time and hourly time predictions
        currentData['datetime'] = pd.to_datetime(currentData['datetime'])
        hourlyData['datetime'] = pd.to_datetime(hourlyData['datetime'])

        #changing the hour to the current hour
        avgD.hour = currentData['datetime'].dt.hour.iloc[0]

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
                todayPrediction = getPrediction(avgData)
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
    except Exception as e:
        print(f"An error occurred in obtainingCurrentHourlyData: {e}")
def get_date():
    try:
        mtoday = date.today()
        mtoday = mtoday.strftime('%A %b %d')
        todayStatement = str(mtoday)
        return todayStatement
    except Exception as e:
        print(f"an error occurred in get_date: {e}")

def get_tomorrow_date():
    try:
        today = date.today()
        tomorrow = today + timedelta(days=1)
        tomorrow = tomorrow.strftime('%A %b %d')
        dateStatement = str(tomorrow)
        return dateStatement
    except Exception as e:
        print(f"an error occurred in get_tomorrow_date: {e}")

def thePredictionsofAPI(avgD, avgData):
    global todayPrediction

    # create the prediction
    try:
        tomorrowPrediction = getPrediction(avgData)
        tomorrowPrediction = tomorrowPrediction[0]
        #get date for today
        today = get_date()
        todayStatment = today + str(todayPrediction) + " inches"
        #get date for tomorrow
        tomorrow = get_tomorrow_date()
        tomorrowStatment = tomorrow + str(tomorrowPrediction) + " inches"

        #putting predictions in json file for UI
        toJson(todayPrediction, tomorrowPrediction, today, tomorrow)

        print(todayStatment)
        print(tomorrowStatment)
        avgD.iterateHour()
    except Exception as e:
        print(f"An error occurred in thePredictionsofAPI: {e}")

#converting the predictions to a json file for the UI
def toJson(todayPrediction, tomorrowPrediction, todayDate, tomorrowDate):
    with open("../react-app/src/predictions.json", mode="w") as file:
        data = {
            "Todays_Prediction": todayPrediction,
            "Tomorrows_Prediction": tomorrowPrediction,
            "Todays_Date": todayDate,
            "Tomorrows_Date": tomorrowDate
         }
        json.dump(data, file)

if __name__ == "__main__":
    main()