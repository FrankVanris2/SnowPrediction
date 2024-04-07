Developers: Conrad Nark, Fed Polyanskiy, Frank Vanris, Trong Duong<br>
Date Started: 4/4/2024<br>
Total Hours: 8<br>
Number of weeks till deadline: 12

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
>(3) The KNN algorithm is supposed to identify the nearest neighbors of a given qury point, so that we can assign a class label to that point.<br>
>(4) If the model does not give well accurate predictions, use NN instead.<br>
>(5) NN uses a different process which we don't have to get into till we complete KNN.

2. Get Data from API then parse Data.<br>
> use:<br>
>(1) We will be obtaining Snoqualmie snow fall data from an API then parse through it using techniques within Python.<br>
>(2) Data can get complex so if needed we can use regex techniques to parse a webpage with data already.<br>

3. Make predictions with the data using the Learning models<br>
>steps:<br>
>(1) Obtain the features and the label for our data. X is for features and y is for the label. <br>
>(2) Split the data to obtain the training and testing sets.<br>
>(3) Choose the model that we would like to train our data on (in our case KNN).<br>
>(4) Instantiate the model, then fit the model to the data.<br>
>(5) Then we predict on the data and obtain the accuracy if needed.<br>

4. Project those predictions then compare it with past predicitons.<br>
>steps:<br>
>(1) Once obtained the predictions compare it with past predictions.<br>
>(2) If needed tweek the algorithm, see and compare consistently with the data. Decide whether if NN is needed to project better predictions.<br>
>(3) use any given visual library to project the data for practicing purposes.<br>
>(4) If needed use Residual plotting to compare between given predictions<br>
>(5) (optional) Use lasso or ridge regression to see how accurate the given predictions are to the actual data.<br>

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
>(4) send data through packet intel and obtain the data from the api and follow the same steps as before when obtaining the data. Thus giving us (hopefully) better predicitons.


