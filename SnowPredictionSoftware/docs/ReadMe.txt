Authors: Frank Vanris, Conrad Nark, Stefana Ciustea
Date: 4/9/2024
Desc: This project basically encompasses predictions of snowfall in snoqualmie pass. There are 3 important python files to look
through:

1. snowAPIMain.py
2. prediction_code.py
3. WeatherAPI.py

within these files they contain the main skeleton and brain of this project. To run the api you need to be in the main.
you can pass in args within the main as well in order to obtain the data now. However, if you do not pass any args it will take
consistent hourly data from the api and average it with the hourly predictions of weather that they api offers so that then it can
be run through the KNN model to create predictions in how much snow will fall for that day.

Unit Tests: There are 2 unit test files within this project that you can test:

1. APISnowPredTesting.py
2. model_unit_test.py

Each of these files tests the mechanics for averaging data and how accurate our model is. No Unit tests are needed for the API,
instead I've created exclusive exceptions within the main to justify whether the network is up or down for the API if issues were
to occur when it comes to retrieving data from the API itself.

Past Resources: that directory contains files that were used during testing purposes and possible ideas for our project that were
then rejected due to a whole team agreement that was needed to know what we should use and not use when it comes to our software.

Relevant Data: This directory contains the relevant features and target features that are needed for our KNN algo to make predictions on the data
that we pass in