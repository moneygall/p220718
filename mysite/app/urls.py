from django.urls import path
from . import views

app_name= "app"

urlpatterns=[
    path('', views.IndexView.as_view(), name= "index"),
    path("send_data/", views.SendData),
    path("recieve_data/", views.RecieveDataView.as_view(), name="recieve_data")
]
