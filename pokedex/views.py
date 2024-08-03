from django.shortcuts import render, get_object_or_404
from .models import Pokemon, Trainer  

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()  #entrenadores
    return render(request, 'index.html', {'pokemons': pokemons, 'trainers': trainers})

def pokemon(request, pokemon_name):
    pokemon = get_object_or_404(Pokemon, name=pokemon_name)
    return render(request, 'display_pokemon.html', {'pokemon': pokemon})

def display_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    return render(request, 'display_pokemon.html', {'pokemon': pokemon})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
