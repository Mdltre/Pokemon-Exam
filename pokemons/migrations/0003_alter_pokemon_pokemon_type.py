# Generated by Django 4.2.1 on 2023-05-10 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0002_remove_species_evolves_from_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='pokemon_type',
            field=models.ManyToManyField(related_name='types', to='pokemons.type'),
        ),
    ]
