from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pokemons.models import Type, Species, Pokemon
from pokemons.forms import PokemonForm

# Create your views here.
class PokemonListView(ListView):
    model = Pokemon
    queryset = Pokemon.objects.all()
    context_object_name = "pokemon_list"
    template_name = "pokemon_list.html"
    
class PokemonDetailView(DetailView):
    model = Pokemon
    context_object_name = "pokemon"
    template_name = "pokemon_details.html"
    
    def get_object(self):
        return get_object_or_404(Pokemon, pk=self.kwargs.get("pokemon_id"))
    
class CreatePokemonView(CreateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = "create_pokemon.html"
    success_url="/list/"
    
class UpdatePokemonView(UpdateView):
    model = Pokemon 
    form_class = PokemonForm
    context_object_name = "pokemon"
    template_name = "update_pokemon.html"
    success_url = "/list/"
    
    def get_object(self):
        return get_object_or_404(Pokemon, pk=self.kwargs.get("pk"))
    
class DeletePokemonView(DeleteView):
    model = Pokemon
    template_name = "delete_pokemon.html"
    success_url = "/list/"