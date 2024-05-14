'''
By: Frank Vanris, Stefana Ciustea
Date: 5/14/2024
Desc: Creating the Unit Tests
'''

import unittest

#This class will inform the test cases that we would like to test to see if our snow prediction site works or not.
class TestSnowPrediction(unittest.TestCase):

    #testing UI
    def test_UI(self):
        self.assertEqual(UI_ON(), 'true')

    #testing prediction accuracy is above 80%
    def test_KNN_Accuracy(self):
        self.assertTrue(accuracyKNN() > 80)

    #testing connection to server
    def test_connection_HTTP(self):
        self.assertEqual(HTTPCon(), 'true')
