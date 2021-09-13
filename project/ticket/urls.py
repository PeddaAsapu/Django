from django.urls import path
from . import views

urlpatterns = [
    path('',views.search,name = "passenger_search"),
    path('passenger',views.passenger,name = "passenger_details"),
    path('temperature',views.temperature,name = "temperature"),
    path('email',views.email,name="email"),
    #path('',views.passenger, name = "passenger"),
    #<int:passenger_id>
]

