import requests
from django.core.management.base import BaseCommand
from django.shortcuts import render
from pokemons.models import Type

class Command(BaseCommand):
    help = "Imports pokemon type names."
    
    def handle(self, *args, **options):
        url = "https://pokeapi.co/api/v2/type/"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            for items in data['results']:
                type_name, _ = Type.objects.get_or_create(
                    type_name=items['name']
                )
            self.stdout.write(f"Added { type_name } to the database.")