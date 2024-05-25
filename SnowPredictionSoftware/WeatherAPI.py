'''
By: Frank Vanris
Date 5/25/2024
Desc: This is the weather api that obtains the given information from a weather station with current data,
and parses it through a csv file.
'''

import urllib.request
import csv

url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/snoqualmie%20pass?unitGroup=metric&include=current&key=32HQHPU2CHJJAH9EGKQGS82DF&contentType=csv"

try:
    # Download the CSV file from the URL
    urllib.request.urlretrieve(url, "snoqualmie_pass_current.csv")

    # Now you can read the local CSV file using pandas or any other library
    # For example, using pandas:
    import pandas as pd
    df = pd.read_csv("snoqualmie_pass_current.csv")
    print(df.head())  # Display the first few rows of the DataFrame
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")