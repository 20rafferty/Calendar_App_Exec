from app import app

# jsonify works the same way that JSON.stringify does
# request is what allows us to take in parameters in the api call
from flask import render_template, jsonify, request

# don't confuse with request method above, requests is a library for calling api's, it is  specific to python, where request above is specific to flask
import requests


# index is going to call weather api and show information on front
@app.route('/')
@app.route('/index')
def index():
    API_KEY = app.config['WEATHER_API_KEY']
    # print(API_KEY)

    city = 'boston'

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=imperial'

    #json() method convets string response into python dictionary
    response = requests.get(url).json()

    print(response)
    return render_template('index.html', response=response)

@app.route('/calendar')
def calendar():
    print("something important")
    return render_template('Calendar.html')
