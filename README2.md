Developers: Conrad Nark, Frank Vanris, Stefana Ciustea <br>
Date Started: 4/4/2024<br>
Total Hours: 38<br>
Number of weeks till deadline: 10

SnowPrediction Project:

# Description
 Creating a Learning Model that can predict whether if it is going to snow or not in snoqualmie pass.

Goal: Range data from a certain amount of years, Create predictions from them, test it upon recent data, then tune the algorithm as much as possible to get it close
to other examples of predictions.


# Requirements

1. Create a learning model (KNN, NN).<br>
> steps:<br>
>(1) In python we will be creating the KNN algorithm for the KNN learning model.<br>
>(2) Skilearn contains a library, if creating the KNN gets to complex we can use the library.<br>
>(3) The KNN algorithm is supposed to identify the nearest neighbors of a given query point, so that we can make a prediction on the target feature (snowfall) for that point.<br>
>(4) If the model does not give well accurate predictions, use neural network instead.<br>
>(5) neural network uses a different process which we don't have to get into till we complete KNN.

2. Get Data from API then parse Data.<br>
> use:<br>
>(1) We will be obtaining Snoqualmie snow fall data from an API then parse through it using techniques within Python.<br>
>(2) Data can get complex so if needed we can use regex techniques to parse a webpage with data already.<br>

3. Make predictions with the data using the Learning models<br>
>steps:<br>
>(1) Determine the most relevant features through data understanding. <br>
>(2) Split the data to obtain the training and testing sets.<br>
>(3) Test various values ok K and sets of features to find the model that produces the best predictions.<br>

4. Project those predictions then compare it with past predicitons.<br>
>steps:<br>
>(1) If needed tweek the algorithm, see and compare consistently with the data. Decide whether if neural network is needed to project better predictions.<br>
>(2) Use any given visual library to project the data for practicing purposes.<br>
>(3) If needed use Residual plotting to compare between given predictions<br>
>(4) Compare best models predictions with commercial predictions for those same data points.<br>

5. If good, create user interface for software.<br>
> steps:<br>
>(1) Create friendly methods that will allow the user to visually know what is happening.<br>
>(2) Create input and output features for the user to use.<br>
>(3) Allow the user to easily access the data without to much searching.<br>
>(4) Allow the user to see past and recent data, with given intervals that we would create.<br>
>(5) Design of user interface will be our choice so we can freely do what we want here.<br>

6. If all progresses good create a weather station for more data.<br>
> steps:<br>
>(1) Create a weather station using an arduino/esp32 microcontroller and sensory devices.<br>
>(2) Obtain Data from the microcontroller and send data through networking protocols.<br>
>(3) Battery usage can be done in different ways either connecting to a port, or for fun cause why not: SOLAR POWER...please guys.<br>
>(4) Send data through packet intel and obtain the data from the api and follow the same steps as before when obtaining the data. Thus giving us (hopefully) better predicitons.


