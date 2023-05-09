from django.contrib import admin

# Register your models here.
from pokemons.models import (
    Type,
    Species,
    Pokemon
)

class TypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["type_name"]}),  
    ]
    
    list_display = ["type_name"]
    
class SpeciesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["species_name", "evolves_from_species", "evolution_chain"]}),
    ]
    
class PokemonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["pokemon_name", "base_experience", "pokemon_sprite", "pokemon_species", "pokemon_type", "pokemon_height", "pokemon_weight"]}),
    ]
    
admin.site.register(Type, TypeAdmin)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Pokemon, PokemonAdmin)