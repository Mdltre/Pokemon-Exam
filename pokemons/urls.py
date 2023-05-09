from django.urls import path, include
from pokemons import views

urlpatterns = [
    path("list/", views.PokemonListView.as_view(), name='pokedex'),
    path("pokemons/<int:pokemon_id>", views.PokemonDetailView.as_view(), name='pokemon-information'), 
]
