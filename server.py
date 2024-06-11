
#Flask is a web server
from flask import Flask

#Sets the name for the web server
app = Flask(__name__)

#these are the routes for the web server
@app.get("/")
def getIndexHtml():
    with open('./index.html') as file:
        return file.read()

@app.get("/dist/main.min.js")
def getMainMinJs():
    with open('./dist/main.min.js') as file:
        return file.read()

@app.get("/api/prediction")
def getPrediction():
    with open('./SnowPredictionSoftware/ImportantJson/predictions.json') as file:
        return file.read()