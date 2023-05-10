from django.forms import ModelForm
from django import forms
from pokemons.models import Type, Species, Pokemon
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PokemonForm(ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"
    
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]