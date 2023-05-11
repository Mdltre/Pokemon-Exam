from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from pokemons.models import Pokemon, Type, Species

class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='user2', email='user2@email.com', password='password')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_valid_login(self):
        response = self.client.post(reverse('login'), {'username': 'user2', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('pokedex'))

    def test_wrong_pass_login(self):
        response = self.client.post(reverse('login'), {'username': 'user2', 'password': 'helloworld'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')
        
    def test_wrong_user_login(self):
        response = self.client.post(reverse('login'), {'username': 'user3', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')
        
class LogoutTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username="user2", email="user2@gmail.com", password="password")
        self.client.force_login(self.user)

    def test_successful_logout(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

class SearchPokemon(TestCase):
    def setUpPokemon(self):
        self.client = Client()
        self.type1 = Type.objects.create(
            type_name='grass', 
            )
        self.type2 = Type.objects.create(
            type_name='poison',
            )
        self.species = Species.objects.create(
            species_name ='bulbasaur',
            evolution_chain = 'https://pokeapi.co/api/v2/evolution-chain/1/'
        )
        self.pokemon = Pokemon.objects.create(
            pokemon_name = 'bulbasaur',
            base_experience = '64',
            pokemon_sprite = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png',
            pokemon_height = '7',
            pokemon_weight = '69'
        )
        self.pokemon.types.add(self.type1, self.type2)
        self.pokemon.species.add(self.species)
        
    def testPokemon_Search(self):
        user=User.objects.create_superuser(username='hello', password='world')
        self.client.force_login(user)
        query = "bul"
        response = self.client.get(reverse("pokedex"),{"q": query})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["pokemon_list"],
            [p for p in Pokemon.objects.filter(pokemon_name__icontains=query)]
        )