# pokedex/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/<str:pokemon_name>/', views.pokemon, name='pokemon'),
]
