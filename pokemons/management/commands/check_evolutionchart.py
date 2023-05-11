import requests
from django.core.management.base import BaseCommand
from django.shortcuts import render
from pokemons.models import Type, Species, Pokemon

class Command(BaseCommand):
    help = "Checks if pokemon evolutions can be accessed through species."
    
    def handle(self, *args, **options):
        pokemon = "squirtle"
        second = None
        third = None
        species_url = f"https://pokeapi.co/api/v2/pokemon-species/{ pokemon }"
        
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
            
            if third != (None):
                
                thirdpic = Pokemon.objects.get(pokemon_name=third)
                secondpic = Pokemon.objects.get(pokemon_name=second)
                firstpic = Pokemon.objects.get(pokemon_name=first)
                print (first + " -> " + second + " -> " + third)
            
            elif second != (None):
                print (first + " -> " + second)
                
            else:
                print (first)