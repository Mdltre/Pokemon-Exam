from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone, timedelta

class Type(models.Model):
    type_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.type_name}"

class Species(models.Model):
    species_name = models.CharField(max_length=100, unique=True)
    evolution_chain = models.URLField(null=True)
   
    def __str__(self):
        return f"{self.species_name}"
class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=100, unique=True)
    base_experience = models.CharField(max_length=5, null=True)
    pokemon_sprite = models.URLField(null=True)
    pokemon_species = models.ForeignKey("pokemons.Species", on_delete=models.CASCADE, related_name="pokemons")
    pokemon_type = models.ManyToManyField("pokemons.Type", related_name="types")
    pokemon_height = models.IntegerField()
    pokemon_weight = models.IntegerField()
    
    def __str__(self):
        return f"{self.pokemon_name}"