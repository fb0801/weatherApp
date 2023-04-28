from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    #url = "https://api.openweathermap.org/data/2.5/weather?={}&units=metric&appid="
    #url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid='
    url ='https://api.openweathermap.org/data/2.5/weather?q={}&appid='
    city = "London"

    r = requests.get(url.format(city)).json()

    city_weather = {
    'city': city,
    'temperature': r['main']['temp'],
    'description': r['weather'][0]['description'],
    'icon':r['weather'][0]['icon'],

    }
    context = {'city_weather': city_weather}
    return render(request, 'weather/weather.html', context)