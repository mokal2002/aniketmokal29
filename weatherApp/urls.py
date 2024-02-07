from django.urls import path
from . import views

urlpatterns = [
    path('weatherApp/', views.weatherApp, name='weatherApp'),
]