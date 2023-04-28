import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    #url = "https://api.openweathermap.org/data/2.5/weather?={}&units=metric&appid="
    #url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid='
    url ='https://api.openweathermap.org/data/2.5/weather?q={}&appid='
    city = "London"

    if request.method == 'POST':
        pass

    form = CityForm()


    cities = City.objects.all()

    weather_data=[]

    for city in cities:

        r = requests.get(url.format(city)).json()
        temp = int(r['main']['temp'] - 273.15) #convert the temperature to C degrees

        city_weather = {
        'city': city.name,
        'temperature': temp,
        'description': r['weather'][0]['description'],
        'icon':r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)