from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Passenger
import requests
import json
import math
# Create your views here.


def search(request):
    #Each_Passenger_details = Passenger.objects.get(id = given_id)
    return render(request,'passengers/search.html', {})


def passenger(request):
    given_id  = request.POST['searched']
    all_passengers = Passenger.objects.get(id=given_id)
    return render(request,'passengers/index.html', {'passengers' : all_passengers})
    
def temperature(request):

    if request.method =="POST":
        city_given = request.POST['city']
        appid = "appid=5cac6a9ab0b0f4798f0b21a31cd45eca"
        link = "https://api.openweathermap.org/data/2.5/weather?q="
        And = "&"
        url = link + city_given + And + appid
        response = requests.get(url)
        json_response = json.loads(response.text)
        temperature = math.ceil((json_response["main"]["temp"] - 273.15))
        string = f"Tempearture in {json_response['name']} is {temperature} Degrees Celsius and {json_response['weather'][0]['description']}"
        return render(request,'passengers/search.html', {'WeatherData' : json_response})
    else:
        return render(request,'passengers/search.html', {})
    #return HttpResponse(string)
