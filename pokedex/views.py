from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Pokemon, Trainer  
from .forms import PokemonForm, TrainerForm

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

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = PokemonForm()
    return render(request, 'add_pokemon.html', {'form': form})

@login_required
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = TrainerForm()
    return render(request, 'add_trainer.html', {'form': form})


@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'edit_pokemon.html', {'form': form})


@login_required
def edit_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'edit_trainer.html', {'form': form})