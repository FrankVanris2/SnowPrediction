'''
By: Frank Vanris, Stefana Ciustea, Conrad Nark
Date: 5/14/2024
Desc: Creating the Unit Tests
'''

import unittest

#This class will inform the test cases that we would like to test to see if our snow prediction site works or not.
class TestSnowPrediction(unittest.TestCase):


    #testing Data / KNN Algorithm
    def test_Retrieve_Data(self):
        self.assertTrue(getData())
    #testing prediction accuracy is above 80%
    def test_KNN_Accuracy(self):
        self.assertTrue(accuracyKNN() > 80)

    #if accuracy is above most learning models
    def test_KNN_Accuracy_AboveAverage(self):
        self.assertTrue(accuracyKNN() > 90)

    #UI / Server
    #testing connection to server
    def test_connection_HTTP(self):
        self.assertTrue(HTTPCon())

    # testing UI
    def test_UI(self):
        self.assertTrue(UI_ON(), 'true')
