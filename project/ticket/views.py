from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Passenger
import requests
import json
import math
from django.core.mail import send_mail
import config
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
        appid = config.api_key
        link = config.api_url
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


# python -m smtpd -n -c DebuggingServer localhost:1025
#local host and port number have been specified in settings file




def email(request):
    if request.method == "POST":
        email_to_find = request.POST['find_email']
        error_message = "Email ID not found"
        valid = True
        try:
            passenger_details = Passenger.objects.get(email=email_to_find)
        except:
            valid = False
        if valid:

            send_mail(
                    f'Hey {passenger_details.passenger_name} Your account info is here !!',
                    f'name: {passenger_details.passenger_name}, mobile : {passenger_details.mobile}, age : {passenger_details.age} , DOB : {passenger_details.dob}',
                    'Donotreply@gmail.com',
                    [passenger_details.email],
                    fail_silently=True,
)
            return render(request,'passengers/search.html',{"passenger_details":passenger_details})
        else:
            return render(request,'passengers/search.html',{"error_message":error_message})
    else:
         return render(request,'passengers/search.html',{})