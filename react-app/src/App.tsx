// src/App.tsx

import React, { useState, useEffect } from 'react';
import './App.css';
import logo from './logo.jpg';
import WeatherCard from './WeatherCard';

function App() {
  const [weatherData, setWeatherData] = useState(null);
  const [showSnowfall, setShowSnowfall] = useState(false);

  const handleGetForecast = () => {
    fetch('https://api.openweathermap.org/data/2.5/forecast?q=Snoqualmie Pass&units=imperial&appid=YOUR_API_KEY')
      .then(response => response.json())
      .then(data => {
        const tomorrow = data.list[1]; // get tomorrow's weather data
        setWeatherData(tomorrow);
        setShowSnowfall(true);
      });
  };

  return (
    <div className="App">
      <div className="banner">
        <h2 className="project-title">Snoqualmie Pass Snowfall</h2>
        <img src={logo} alt="Logo" className="logo" />
      </div>
      <div className="container">
        <div className="button-container">
          <button onClick={handleGetForecast} className="get-forecast-button">Get Forecast</button>
        </div>
        {weatherData && (
          <WeatherCard
            date="Today"
            icon="01d"
            temp={65}
            snowfall={2}
            unit="°F"
            description="Sunny with a chance of snow"
          />
        )}
      </div>
    </div>
  );
}

export default App;