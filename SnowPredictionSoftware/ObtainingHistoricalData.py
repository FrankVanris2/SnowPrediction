'''
Authors: Frank Vanris
Date: 4/12/2024
Desc: Creating a dataframe with all of the needed data to be sent into the KNN learning model
'''

#my imports
import pandas as pd

#creating a function that will contain the historical data needed for the KNN algorithm
    #obtaining historical data
listHistoricalData = []
for year in range(2016,2023):
    historicalData = pd.read_csv("data\\SnoqualmiePass_3010_" + str(year) + ".csv")

    #removing Solar Radiation from the 2016 data since it's the only one that has it
    if year == 2016:
        historicalData = historicalData.drop('Solar Radiation  (W/m2) ', axis='columns')

    #reducing 1 column from each of our data since we don't need to know the total snow depth, Battery Voltage, and Solar Radiation
    historicalData = historicalData.drop(['Battery Voltage  (v) ', 'Total Snow Depth  (") '], axis=1)


    #reducing the number of rows to the days and months of Jan 1st - May 1st and Nov 15th - Dec 31st

     #Filtering Data In DataFrame
    historicalData = historicalData.loc[(historicalData['Date/Time (PST)'] >= str(year) + '-01-01') &
                    (historicalData['Date/Time (PST)'] <= str(year) + '-05-01') |
                    (historicalData['Date/Time (PST)'] >= str(year) + '-11-15') &
                    (historicalData['Date/Time (PST)'] <= str(year) + '-12-31T23:59:59')]

    #reverse the data to Jan 1st to Dec 31st
    historicalData = historicalData.iloc[::-1]

    listHistoricalData.append(historicalData)

totalHistoricalData = pd.concat(listHistoricalData)

#putting totalHistoricalData into a csv
totalHistoricalData.to_csv('TotalHistoricalData.csv', index=False)