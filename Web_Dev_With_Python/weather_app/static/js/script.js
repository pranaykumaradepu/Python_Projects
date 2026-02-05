const cityInput = document.getElementById('cityInput');
        
        cityInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                const city = cityInput.value;
                fetchWeather(city);
            }
        });

        async function fetchWeather(city) {
            // This calls our REST API endpoint
            const response = await fetch(`/api/weather/${city}`);
            const data = await response.json();

            if (response.ok) {
                // Update the UI without refreshing!
                document.getElementById('welcomeMessage').style.display = 'none';
                document.getElementById('weatherDisplay').style.display = 'block';
                
                document.getElementById('cityName').innerText = data.city;
                document.getElementById('tempDisplay').innerText = data.temp + '°';
                document.getElementById('description').innerText = data.desc;
                document.getElementById('humidity').innerText = data.humidity;
                document.getElementById('wind').innerText = data.wind;
                document.getElementById('weatherIcon').src = `http://openweathermap.org/img/wn/${data.icon}@2x.png`;
            } else {
                alert("City not found!");
            }
        }