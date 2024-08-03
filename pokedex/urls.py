
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('pokemon/<int:pokemon_id>/', views.display_pokemon, name='display_pokemon'),
    path('pokemon/<str:pokemon_name>/', views.pokemon, name='pokemon'),
    path('add_pokemon/', views.add_pokemon, name='add_pokemon'),
    path('add_trainer/', views.add_trainer, name='add_trainer'),
    path('edit_pokemon/<int:pokemon_id>/', views.edit_pokemon, name='edit_pokemon'),
    path('edit_trainer/<int:trainer_id>/', views.edit_trainer, name='edit_trainer'),

]
