from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone, timedelta

# Create your models here.

class Type(models.Model):
    type_name = models.CharField(max_length=100, unique=True)

class Species(models.Model):
    species_name = models.CharField(max_length=100, unique=True)
    evolves_from_species = models.URLField(null=True)
    evolution_chain = models.URLField(null=True)
    
class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=100, unique=True)
    base_experience = models.CharField(max_length=5, null=True)
    pokemon_sprite = models.URLField(null=True)
    pokemon_species = models.ForeignKey("pokemons.Species", on_delete=models.CASCADE, related_name="pokemons")
    pokemon_type = models.ManyToManyField("pokemons.Type")
    pokemon_height = models.IntegerField()
    pokemon_weight = models.IntegerField()
    
