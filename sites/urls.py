from django.urls import path
from . import views

app_name='sites'
urlpatterns = [
    path('', views.home, name='home'),
]

