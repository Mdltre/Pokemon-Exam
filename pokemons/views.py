from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from pokemons.models import Type, Species, Pokemon
from django.contrib.auth.decorators import user_passes_test, login_required
from pokemons.forms import PokemonForm, RegistrationForm

# Create your views here.

class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy('login')
    
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
        return get_object_or_404(Pokemon, pk=self.kwargs.get("pk"))
    
class CreatePokemonView(CreateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = "create_pokemon.html"
    success_url="pokedex/list/"
    
class UpdatePokemonView(UpdateView):
    model = Pokemon 
    form_class = PokemonForm
    context_object_name = "pokemon"
    template_name = "update_pokemon.html"
    success_url = "/pokedex/list/"
    
    def get_object(self):
        return get_object_or_404(Pokemon, pk=self.kwargs.get("pk"))
    
class DeletePokemonView(DeleteView):
    model = Pokemon
    template_name = "delete_pokemon.html"
    success_url = "/pokedex/list/"
    
class SearchPokemonView(ListView):
    model = Pokemon
    template_name = "pokemon_list.html"
    context_object_name = "pokemons"
    
    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            return Pokemon.objects.filter(pokemon_name__contains=query)
    
class FilterTypePokemonView(ListView):
    model = Pokemon
    template_name = "pokemon_list.html"
    context_object_name = "pokemons"
    
    def get_queryset(self):
        query = self.request.GET.get("types")
        if query:
            
            return Pokemon.objects.filter(types__in=[query])
        
