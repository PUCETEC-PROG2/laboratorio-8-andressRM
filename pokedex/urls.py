# pokedex/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('pokemon/<int:pokemon_id>/', views.display_pokemon, name='display_pokemon'),  # Nueva ruta para la vista por ID
    path('pokemon/<str:pokemon_name>/', views.pokemon, name='pokemon'),
    path('trainers/', views.trainers, name='trainers'),
]
