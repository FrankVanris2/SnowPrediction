'''
By: Conrad Nark
Date: 5/05/2024
Desc: This uses the KNN learning model to create predictions of snowfall data within a 24 hour period.
'''

from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

def getFeatures():
    return pd.read_csv("RelevantData/HistoricalRelevantData/kNNReadyFeatures.csv")

def getscaledFeatures():
    df = pd.read_csv("RelevantData/HistoricalRelevantData/kNNReadyScaledFeatures.csv")
    return df

def getTargetFeature():
    return pd.read_csv("RelevantData/HistoricalRelevantData/actualFinalizedSnow.csv")

def getPrediction(todaysWeather):
    features = getFeatures()

    #appending my current Weather to the none scale
    features = features._append(todaysWeather, ignore_index=True)

    scaledfeatures = getscaledFeatures()

    targetFeatures = getTargetFeature()
    #THIS IS WHAT I ADDED
    targetColumn = targetFeatures['24HourSnow']
    #scalar object
    scalar = MinMaxScaler()
    #scale query data point
    todaysWeatherScaled = scalar.fit_transform(features)
    #return to DF with correct column names
    todaysWeatherScaled = pd.DataFrame(todaysWeatherScaled,columns=features.columns)
    #KNN_Regressor is the object that is the model
    KNN_Regressor = KNeighborsRegressor(n_neighbors=23,weights='distance',algorithm='ball_tree',p=1)
    #fit it features and target features for the model
    KNN_Regressor.fit(scaledfeatures, targetColumn)
    #make the prediction
    series = todaysWeatherScaled.iloc[-1]
    features = None
    df = pd.DataFrame([series])
    prediction = KNN_Regressor.predict(df)
    #return rounded prediction
    return np.rint(prediction)
    
