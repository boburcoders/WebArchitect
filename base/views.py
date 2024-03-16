from django.shortcuts import render

# Create your views here.


from django.core.cache import cache
from django.shortcuts import render
import requests

from django.http import JsonResponse
from .models import WeatherData

API_KEY = 'b19ef47e383821acf92694c11bf2f394'


def get_weather(request, city):
    # Check if weather data is cached
    # cached_weather_data = cache.get('cached_weather_data')
    #
    # if cached_weather_data:
    #     weather_data = cached_weather_data
    # else:
    # Fetch weather data from external API
    # city = "Manchester"  # Default city for this example
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    json_res = response.json()

    # Extract relevant weather data from the API response
    temperature = json_res['main']['temp'] - 272.15  # Convert temperature from Kelvin to Celsius
    pressure = json_res['main']['pressure']
    description = json_res['weather'][0]['description']

    # Save weather data to the database
    weather_data = WeatherData.objects.create(city_name=city, description=description,
                                              temperature=temperature, pressure=pressure)

        # cache.set('cached_weather_data', weather_data, timeout=60*5)


def get_weather_by_city(request, city_name):
    # Query the database for WeatherData objects with the given city_name
    try:
        get_weather(request, city_name)
    except:
        return JsonResponse({"message": "City not found"}, status=404)

    weather_data = WeatherData.objects.filter(city_name=city_name).last()

    if weather_data:
        # Serialize the retrieved data
        serialized_data = {
            "city_name": weather_data.city_name,
            "pressure": weather_data.pressure,
            "temperature": weather_data.temperature,
            "description": weather_data.description,
            "updated": weather_data.updated.strftime("%Y-%m-%d %H:%M:%S")
        }
        # Return the serialized data as a JSON response
        return JsonResponse(serialized_data)
    else:
        # If no data found for the given city_name, return a 404 response
        return JsonResponse({"error": "Data not found for the specified city"}, status=404)


def get_city_input(request):
    city = request.GET.get('city')

    # Check if city is provided
    if city:
        # Check if weather data is cached
        cached_weather_data = cache.get('cached_weather_data')

        if cached_weather_data:
            weather_data = cached_weather_data
        else:
            # Retrieve the last weather data for the city from the database
            last_data = WeatherData.objects.filter(city_name=city).last()

            if last_data:
                weather_data = last_data
            else:
                # Fetch weather data from external API
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
                response = requests.get(url)
                json_res = response.json()

                # Extract relevant weather data from the API response
                temperature = json_res['main']['temp'] - 272.15  # Convert temperature from Kelvin to Celsius
                pressure = json_res['main']['pressure']
                description = json_res['weather'][0]['description']

                # Save weather data to the database
                weather_data = WeatherData.objects.create(city_name=city, description=description,
                                                          temperature=temperature, pressure=pressure)

                # Cache the weather data for future requests (cache for 1 hour in this example)
                cache.set('cached_weather_data', weather_data, timeout=60)

        return render(request, 'index.html', {"last_data": weather_data})

    else:
        return render(request, 'index.html', {"error_message": "Please provide a city name."}, status=404)
