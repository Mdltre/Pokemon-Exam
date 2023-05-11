from typing import Any, Dict
import requests
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from pokemons.models import Type, Species, Pokemon
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator
from pokemons.forms import PokemonForm, RegistrationForm


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy('login')
    
class PokemonListView(ListView):
    model = Pokemon
    context_object_name = "pokemon_list"
    template_name = "pokemon_list.html"
    
    def get_queryset(self):
        t_query = self.request.GET.get("types")
        query = self.request.GET.get("query")
        
        if t_query:
            result = Type.objects.get(type_name__exact=t_query)
            pokemon_result = Pokemon.objects.filter(pokemon_type = result)
            return pokemon_result
        
        elif query:
            return Pokemon.objects.filter(pokemon_name__contains=query)
        
        else:
            return Pokemon.objects.all()
            
    
class PokemonDetailView(DetailView):
    model = Pokemon
    context_object_name = "pokemon"
    template_name = "pokemon_details.html"
    
    def get_object(self):
        return get_object_or_404(Pokemon, pk=self.kwargs.get("pk"))
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemon = self.get_object()
        second = None
        third = None
        second_p = None
        third_p = None
        species_url = f"https://pokeapi.co/api/v2/pokemon-species/{ pokemon.id }"
        
        res = requests.get(species_url)
        if res.status_code == 200:
            data = res.json()
            evolution_url = data["evolution_chain"]["url"]
            e_info = requests.get(evolution_url).json()
            
            first = e_info["chain"]["species"]["name"]
            
            if len(e_info["chain"]["evolves_to"]) > 0:
                
                second = e_info["chain"]["evolves_to"][0]["species"]["name"]
                
                if len(e_info["chain"]["evolves_to"][0]["evolves_to"]) > 0:
                    
                    third = e_info["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]

        if second is not None:
            second_p = Pokemon.objects.get(pokemon_name=second)
            
            if third is not None:
                third_p = Pokemon.objects.get(pokemon_name=third)
            
        first_p = Pokemon.objects.get(pokemon_name=first)
        
        evolution = {
            "third_p": third_p,
            "second_p": second_p,
            "first_p": first_p
        }
        
        context["evolution"] = evolution
        
        return context
                
        

    
@method_decorator(login_required, name='dispatch')
class CreatePokemonView(CreateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = "create_pokemon.html"
    success_url="pokedex/list/"

@method_decorator(login_required, name='dispatch')
class UpdatePokemonView(UpdateView):
    model = Pokemon 
    form_class = PokemonForm
    context_object_name = "pokemon"
    template_name = "update_pokemon.html"
    success_url = "/pokedex/list/"
    
    def get_object(self):
        return get_object_or_404(Pokemon, pk=self.kwargs.get("pk"))

@method_decorator(login_required, name='dispatch')
class DeletePokemonView(DeleteView):
    model = Pokemon
    template_name = "delete_pokemon.html"
    success_url = "/pokedex/list/"
    