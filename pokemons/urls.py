from django.urls import path, include
from pokemons import views

urlpatterns = [
    path("list/", views.PokemonListView.as_view(), name='pokedex'),
    path("pokemons/<int:pk>", views.PokemonDetailView.as_view(), name='pokemon-information'),
    path("pokemons-create/", views.CreatePokemonView.as_view(), name='create-pokemon'),
    path("pokemons-update/<int:pk>", views.UpdatePokemonView.as_view(), name='update-pokemon'),
    path("pokemons-delete/<int:pk>", views.DeletePokemonView.as_view(), name='delete-pokemon')
]
