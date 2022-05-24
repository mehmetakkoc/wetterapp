from django.http import response
from django.shortcuts import render
import requests
from decouple import config
from pprint import pprint
from .models import City

def index(request):
    cities = City.objects.all()
    # url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
    # city ="Berlin"
    # response =requests.get(url.format(city, config("API_KEY")))
    # content = response.json()
    # pprint(content)

    city_data = []
    for city in cities:
        print(city)
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
        # city ="Berlin"
        response =requests.get(url.format(city, config("API_KEY")))
        content = response.json()
        # pprint(content)
        data = {
            "city":content["name"],
            "temp":content["main"]["temp"],
            "desc":content["weather"][0]["description"],
            "icon":content["weather"][0]["icon"],

        
        }
        city_data.append(data)
        

    # pprint(city_data)
    context = {
        "city_data":city_data
        }

    return render(request, 'weatherapp/index.html', context)
