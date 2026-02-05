from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

if not API_KEY:
    raise ValueError("No API_KEY set for Flask application. Check your .env file.")

def get_weather_data(city):
    url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else {"error": "Not Found"}

# This route just loads the initial empty page
@app.route('/')
def index():
    return render_template('index.html')

# 2. THIS IS THE REST API ENDPOINT
@app.route('/api/weather/<city>')
def weather_api(city):
    raw_data = get_weather_data(city)
    
    if 'error' in raw_data:
        return jsonify({'error': 'City not found'}), 404
    
    # We package only the data the frontend needs
    payload = {
        'city': raw_data['name'],
        'temp': int(raw_data['main']['temp']),
        'desc': raw_data['weather'][0]['main'],
        'humidity': raw_data['main']['humidity'],
        'wind': raw_data['wind']['speed'],
        'icon': raw_data['weather'][0]['icon']
    }
    return jsonify(payload) # This sends raw data, not a webpage!

if __name__ == '__main__':
    app.run(debug=True)