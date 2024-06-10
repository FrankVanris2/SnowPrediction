// src/WeatherCard.tsx

import React from 'react';

interface WeatherCardProps {
  date: string;
  icon: string;
  temp: number;
  snowfall: number;
  unit: string;
  description: string;
}

const WeatherCard: React.FC<WeatherCardProps> = ({ date, icon, temp, snowfall, unit, description }) => {
    return (
      <div className="weather-card">
        <h3>{date}</h3>
        <img src={`http://openweathermap.org/img/wn/${icon}@2x.png`} alt={icon} />
        <p>{description}</p>
        <p>Temperature: {temp} {unit}</p>
        <p>Snowfall: {snowfall} inches</p>
      </div>
    );
};

export default WeatherCard;