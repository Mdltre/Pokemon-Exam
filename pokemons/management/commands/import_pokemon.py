import requests
from django.core.management.base import BaseCommand
from django.shortcuts import render
from pokemons.models import Pokemon

class Command(BaseCommand):
    help = "Imports pokemon details from PokeAPI endpoint."
    
    def handle(self, *args, **options):
        url = "https://pokeapi.co/api/v2/pokemon/"
        # params = {'limit': 151} 
        all_pokemons = {}
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            for i in range(0, 151):
                # params['offset'] = offset  # add new value to dict with `limit`
                # response = requests.get(url) # , params=params

                # if response.status_code != 200: 
                #     print(response.text)
                    # data = response.json()
                for pokemons in data['results']:
                    # pokemon_name = pokemons.get('name')
                    pokemon_info = pokemons.get('url')
                        
                    pokemon_data = requests.get(pokemon_info).json()
                    pokemon_name, _ = Pokemon.objects.get_or_create(
                        pokemon_name = pokemon_data['name'],
                        
                    )
                    
                    # pokemons = pokemon_data['abilities']
                    breakpoint()
                        
                    # pokemon_name = (item.get('name'),item.get('sprites'))
                    # print(pokemon_name)
                    # pokemon, _ = Pokemon.objects.get_or_create(pokemon_name = pokemon_name)
                    # self.stdout.write(f"Adding pokemon {pokemon_name} to the database...")

        else:
            self.stdout.write(self.style.ERROR("Failed to import pokemons."))      