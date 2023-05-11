import requests
from django.core.management.base import BaseCommand
from django.shortcuts import render
from pokemons.models import Type, Species, Pokemon


class Command(BaseCommand):
    help = "Imports pokemon species."
    
    def handle(self, *args, **options):
        url = "https://pokeapi.co/api/v2/pokemon-species/?limit=151"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            for items in data['results']:
                species_info = items.get('url')
                species_data = requests.get(species_info).json()
                print(species_data['name'])
                species_details, _ = Species.objects.get_or_create(
                    species_name = species_data['name'],
                    evolution_chain = species_data['evolution_chain']['url']
                )
                self.stdout.write(f"Added { species_details } to the database.")
                
                #add pokemon through pokemon species
                pokemon_url = species_data["varieties"][0]["pokemon"]["url"]
                pokemon_data = requests.get(pokemon_url).json()
                
                pokemon_details, _ = Pokemon.objects.get_or_create(
                    pokemon_name = pokemon_data['name'],
                    base_experience = pokemon_data['base_experience'],
                    pokemon_sprite = pokemon_data['sprites']['front_default'],
                    pokemon_species = species_details,
                    pokemon_height = pokemon_data['height'],
                    pokemon_weight = pokemon_data['weight']
                )
                for types in pokemon_data["types"]:
                    typee = Type.objects.get(type_name=types["type"]["name"])
                    pokemon_details.pokemon_type.add(typee)
                    
                    
                self.stdout.write(f"Added { pokemon_details } to the database.")
        else:
            self.stdout.write(self.style.ERROR("Failed to import pokemon species.")) 