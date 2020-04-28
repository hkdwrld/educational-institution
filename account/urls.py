from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
]
