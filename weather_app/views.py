from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from weather_app.forms import CityForm
from .models import City

# Create your views here.
def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=08fb6b8413c496d611bcec503cc675d7'

    msg = ''
    class_msg = ''

    cities = City.objects.all().reverse()

    weather_data = []
    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            exist = City.objects.filter(name=new_city).count()

            if exist == 0:
                response = requests.get(url.format(new_city)).json()

                if response['cod'] == 200:
                    msg = 'City added successfully'
                    class_msg = 'bg-success'
                    form.save()

                else:
                    msg = "There isn't a city with this name !!!"
                    class_msg = 'bg-danger'

            else:
                msg = 'The city is already exist !!!'
                class_msg = 'bg-danger'

    form = CityForm()

    for city in cities:
        response = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': int((response['main']['temp'] - 32 ) * 5/9),
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
            'id': city.id
        }

        weather_data.append(city_weather)

    print(weather_data)
    context = {
        'weather_data': weather_data,
        'form': form,
        'msg': msg,
        'class_msg': class_msg,
    }

    return render(request, 'weather_app/index.html', context=context)

def delete_city(request, id_city):
    City.objects.get(id=id_city).delete()

    return HttpResponseRedirect('/')
