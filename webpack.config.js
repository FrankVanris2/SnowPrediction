"use strict";

module.exports = {
  mode: 'development',

  output: {
    filename: "main.min.js"
  },

  devtool: 'inline-source-map',

  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /(node_modules)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react'],
            plugins: [
              [
                "styled-components",
                {
                  "ssr": true,
                  "displayName": true,
                  "preprocess": false
                }
              ]
            ]
          }
        }
      }
    ]
  }
};
