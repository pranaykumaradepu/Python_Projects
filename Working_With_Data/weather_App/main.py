# Weather App By openweathermap.org

import requests
import time

# step 1 : Api setup 
api_key = 'Your Api Key'
baase_url = f'https://api.openweathermap.org/data/2.5/weather'

# step 2: Get weather data
def get_weather_data(city):
    try:
        url = f'{baase_url}?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        elif response.status_code == 404:
            print(' City not found')
        else:
            print(f'Error {response.status_code}')
    except Exception as e:
        print(e)

# step 3: Display weather data
def display_weather_data(data):
    try:
        city = data['name']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        # humidity = data.get('main',{}).get('humidity',{})

        print(f'City: {city}')
        print(f'Temperature: {temperature}°C')
        print(f'Description: {description}')
        print(f'Humidity : {humidity}')
        print(f'Wind Spped : {wind_speed}')
    except Exception as e:
        print(e)

# step 4 : Main program
def main():
    while True:
        print('--- Weather App ---')
        city_name = input('\nenter city name to get weather data / q to quit : ').lower()
        if city_name.strip() == 'q':
            print('thank you')
            break
        weather = get_weather_data(city_name)
        if weather:
            display_weather_data(weather)
if __name__ == "__main__": 
    main()
