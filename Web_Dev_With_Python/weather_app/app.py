from flask import Flask, render_template, request
from dotenv import load_dotenv

import requests
import os

# 1. Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# 2. Get the API Key safely
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Check if key loaded correctly (Optional but helpful for debugging)
if not API_KEY:
    raise ValueError("No API_KEY set for Flask application. Check your .env file.")

def get_weather_data(city):
    try:
        url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {'error': 'City not found. Please check the spelling.'}
        else:
            return {'error': f'Error: {response.status_code}'}
            
    except Exception as e:
        return {'error': f'An error occurred: {e}'}

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        
        if city:
            raw_data = get_weather_data(city)
            
            if raw_data and 'error' not in raw_data:
                weather_data = {
                    'city': raw_data['name'],
                    'temperature': int(raw_data['main']['temp']), # Changed to int for cleaner look
                    'description': raw_data['weather'][0]['description'].capitalize(),
                    'condition_main': raw_data['weather'][0]['main'], # <--- ADD THIS LINE
                    'humidity': raw_data['main']['humidity'],
                    'wind_speed': raw_data['wind']['speed'],
                    'icon': raw_data['weather'][0]['icon']
                }
            else:
                weather_data = raw_data

    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)