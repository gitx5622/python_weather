import requests
from django.templatetags.static import static
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import City
from django.db.models import Q

def index(request):
    city_id = 1148416
    WEATHER_API_KEY = '9b010a7a7ac95466fe471aea7816c3d9'
    url_template = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid={}'
    url = url_template.format(city_id, WEATHER_API_KEY)

    data = requests.get(url).json()
    
    city_weather = {
        "city_name": data['name'],
        # 'country_name' : Country.objects.get(code=data['sys']['country']).name,
        'weather': data['weather'][0]['main'],
        'weather_description': data['weather'][0]['description'],
        'temperature': int(round(data['main']['temp'] - 273.15)),
        'humidity': int(round(data['main']['humidity'])),
        'pressure': int(round(data['main']['pressure'])),
        'wind_speed': int(round(data['wind']['speed'])),
        'icon_url': static('images/icons/{}.png'.format(data['weather'][0]['icon']))
    }
    context = {
        'city_weather': city_weather

    }
    return render(request, 'index.html')


def search(request):
    query = request.GET.get('q')
    lookups= Q(name__icontains=query) | Q(id__icontains=query)
    results= City.objects.filter(lookups).distinct()
    
    context = {
        'results':results

    }
    return  render(request, 'index.html',context)
