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
        (None, {"fields": ["species_name", "evolution_chain"]}),
    ]
    search_fields = ["species_name"]
    list_display = ["species_name"]
    
class PokemonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["pokemon_name", "base_experience", "pokemon_sprite", "pokemon_species", "pokemon_type", "pokemon_height", "pokemon_weight"]}),
    ]
    search_fields = ["pokemon_name"]
    list_display = ["pokemon_name"]
    
admin.site.register(Type, TypeAdmin)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Pokemon, PokemonAdmin)