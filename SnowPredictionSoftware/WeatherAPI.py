'''
By: Frank Vanris
Date 5/25/2024
Desc: This is the weather api that obtains the given information from a weather station with current data,
and parses it through a csv file.
'''

import urllib.request
import csv

#Grab api data once an hour
def weatherAPI():
    url1_current = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/snoqualmie%20pass?unitGroup=metric&include=current&key=32HQHPU2CHJJAH9EGKQGS82DF&contentType=csv"
    url2_hourly = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/snoqualmie%20pass?unitGroup=metric&include=hours&key=32HQHPU2CHJJAH9EGKQGS82DF&contentType=csv"

    try:
        # Download the CSV file from the URL
        urllib.request.urlretrieve(url1_current, "RelevantData/snoqualmie_pass_current.csv")
        urllib.request.urlretrieve(url2_hourly, "RelevantData/snoqualmie_pass_hourly.csv")

    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
    except urllib.error.URLError as e:
        print(f"URL Erroar: {e.reason}")


