from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url = "https://api.openweathermap.org/data/2.5/weather?={}&units=metric&appid="
    city = "London"

    r = requests.get(url.format(city)).json()

    city_weather = {
    'city': ,
    'temperature': '',
    'description': '',
    'icon':,

    }

    return render(request, 'weather/weather.html')