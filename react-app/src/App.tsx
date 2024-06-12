// src/App.tsx
//By: Stefana Ciustea
//Date: 5/30/24
//Desc: actual workings of UI design
// src/App.tsx

// Stefana Ciustea
// Gets snowfall prediction for today and tomorrow through the API from the backend

import React, { useState } from 'react';
import './App.css';
import logo from './logo.JPG';
import predictionsData from './predictions.json';

function App() {
  const [todaysPrediction, setTodaysPrediction] = useState<number | null>(null);
  const [tomorrowsPrediction, setTomorrowsPrediction] = useState<number | null>(null);
  const [todaysDate, setTodaysDate] = useState<string | null>(null);
  const [tomorrowsDate, setTomorrowsDate] = useState<string | null>(null);
  const handleGetForecast = () => {
    // accesses the predictions
    const { Todays_Prediction, Tomorrows_Prediction, Todays_Date, Tomorrows_Date } = predictionsData;

    // sets the predictions
    setTodaysPrediction(Todays_Prediction);
    setTomorrowsPrediction(Tomorrows_Prediction);
    setTodaysDate(Todays_Date);
    setTomorrowsDate(Tomorrows_Date);
  };

  return (
    <div className="App">
      <div className="banner">
        <h2 className="project-title">Snoqualmie Pass Snowfall</h2>
        <img src={logo} alt="Logo" className="logo" />
      </div>
      <div className="container">
        <div className="prediction_container">
          {todaysPrediction !== null && (
            <div className="prediction">
              <h4>{todaysDate}</h4>
              <p>{todaysPrediction} inches</p>
            </div>
          )}
          {tomorrowsPrediction !== null && (
            <div className="prediction">
              <h4>{tomorrowsDate}</h4>
              <p>{tomorrowsPrediction} inches</p>
            </div>
          )}
          <div className="button-container">
            <button onClick={handleGetForecast} className="get-forecast-button">Get Predictions</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

