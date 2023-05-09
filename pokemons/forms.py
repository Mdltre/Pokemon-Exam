from django.forms import ModelForm
from django import forms
from pokemons.models import Type, Species, Pokemon

class PokemonForm(ModelForm):
    model = Pokemon
    field = "__all__"
    
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length = 100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())