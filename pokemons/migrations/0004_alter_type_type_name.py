# Generated by Django 4.2.1 on 2023-05-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0003_alter_pokemon_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='type_name',
            field=models.CharField(max_length=100),
        ),
    ]