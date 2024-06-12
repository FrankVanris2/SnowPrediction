'''
By: Conrad Nark
Date: 5/30/2024
Desc: Unit test for KNN Model to make sure our accuracy is below 2
'''

from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import numpy as np
import unittest

class ModelTest(unittest.TestCase):
    
    def test_model_accuracy(self):
        #load features
        featureSet = pd.read_csv('RelevantData/HistoricalRelevantData/kNNReadyScaledFeatures.csv')
        #load target feature
        target = pd.read_csv('RelevantData/HistoricalRelevantData/actualFinalizedSnow.csv')
        #isolate target feature
        target = target['24HourSnow']
        #initalize useful variables
        meanAbsoluteError = 0
        numTests = 1000
        #run numTests tests for k=23 on numTests different test train splits using 90% of testData for model training and
        #10% for testing. 
        for i in range(numTests):
            featuresTrain, featuresTest, targetTrain, targetTest = train_test_split(featureSet,target,test_size=.1)
            KNN_Model = KNeighborsRegressor(n_neighbors=23, weights='distance',algorithm='auto',p=1)
            KNN_Model = KNN_Model.fit(featuresTrain,targetTrain)
            predictions = KNN_Model.predict(featuresTest)
            predictions = np.rint(predictions)
            meanAbsoluteError = mean_absolute_error(targetTest,predictions) + meanAbsoluteError
        #find average mean absolute error over numTests
        meanAbsoluteError = meanAbsoluteError/numTests
        #assert that mean absolute error is less than 2in
        message = "error greater than 2 inches"
        self.assertLess(meanAbsoluteError,2,message)

if __name__ == '__main__':
    unittest.main()

    
