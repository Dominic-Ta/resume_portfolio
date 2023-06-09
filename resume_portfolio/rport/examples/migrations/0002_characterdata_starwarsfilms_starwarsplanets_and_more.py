# Generated by Django 4.2 on 2023-07-11 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("examples", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CharacterData",
            fields=[
                ("index", models.TextField(primary_key=True, serialize=False)),
                ("height", models.TextField(blank=True, null=True)),
                ("mass", models.TextField(blank=True, null=True)),
                ("skin_color", models.TextField(blank=True, null=True)),
                ("hair_color", models.TextField(blank=True, null=True)),
                ("birth_year", models.TextField(blank=True, null=True)),
                ("gender", models.TextField(blank=True, null=True)),
                ("homeworld", models.TextField(blank=True, null=True)),
                ("films", models.TextField(blank=True, null=True)),
                ("species", models.TextField(blank=True, null=True)),
                ("char_num", models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "character_data",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="StarwarsFilms",
            fields=[
                ("index", models.BigIntegerField(primary_key=True, serialize=False)),
                ("title", models.TextField(blank=True, null=True)),
                ("episode_id", models.BigIntegerField(blank=True, null=True)),
                ("opening_crawl", models.TextField(blank=True, null=True)),
                ("director", models.TextField(blank=True, null=True)),
                ("producer", models.TextField(blank=True, null=True)),
                ("release_date", models.TextField(blank=True, null=True)),
                ("characters", models.TextField(blank=True, null=True)),
                ("planets", models.TextField(blank=True, null=True)),
                ("starships", models.TextField(blank=True, null=True)),
                ("vehicles", models.TextField(blank=True, null=True)),
                ("species", models.TextField(blank=True, null=True)),
                ("url", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "starwars_films",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="StarwarsPlanets",
            fields=[
                ("index", models.BigIntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField(blank=True, null=True)),
                ("rotation_period", models.TextField(blank=True, null=True)),
                ("orbital_period", models.TextField(blank=True, null=True)),
                ("diameter", models.TextField(blank=True, null=True)),
                ("climate", models.TextField(blank=True, null=True)),
                ("gravity", models.TextField(blank=True, null=True)),
                ("terrain", models.TextField(blank=True, null=True)),
                ("surface_water", models.TextField(blank=True, null=True)),
                ("population", models.TextField(blank=True, null=True)),
                ("residents", models.TextField(blank=True, null=True)),
                ("films", models.TextField(blank=True, null=True)),
                ("url", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "starwars_planets",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="StarwarsSpecies",
            fields=[
                ("index", models.BigIntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField(blank=True, null=True)),
                ("classification", models.TextField(blank=True, null=True)),
                ("designation", models.TextField(blank=True, null=True)),
                ("average_height", models.TextField(blank=True, null=True)),
                ("skin_colors", models.TextField(blank=True, null=True)),
                ("hair_colors", models.TextField(blank=True, null=True)),
                ("eye_colors", models.TextField(blank=True, null=True)),
                ("average_lifespan", models.TextField(blank=True, null=True)),
                ("homeworld", models.TextField(blank=True, null=True)),
                ("language", models.TextField(blank=True, null=True)),
                ("people", models.TextField(blank=True, null=True)),
                ("films", models.TextField(blank=True, null=True)),
                ("url", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "starwars_species",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="StarwarsStarships",
            fields=[
                ("index", models.BigIntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField(blank=True, null=True)),
                ("model", models.TextField(blank=True, null=True)),
                ("manufacturer", models.TextField(blank=True, null=True)),
                ("cost_in_credits", models.TextField(blank=True, null=True)),
                ("length", models.TextField(blank=True, null=True)),
                ("max_atmosphering_speed", models.TextField(blank=True, null=True)),
                ("crew", models.TextField(blank=True, null=True)),
                ("passengers", models.TextField(blank=True, null=True)),
                ("cargo_capacity", models.TextField(blank=True, null=True)),
                ("consumables", models.TextField(blank=True, null=True)),
                ("hyperdrive_rating", models.TextField(blank=True, null=True)),
                ("mglt", models.TextField(blank=True, db_column="MGLT", null=True)),
                ("starship_class", models.TextField(blank=True, null=True)),
                ("pilots", models.TextField(blank=True, null=True)),
                ("films", models.TextField(blank=True, null=True)),
                ("url", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "starwars_starships",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="StarwarsVehicles",
            fields=[
                ("index", models.BigIntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField(blank=True, null=True)),
                ("model", models.TextField(blank=True, null=True)),
                ("manufacturer", models.TextField(blank=True, null=True)),
                ("cost_in_credits", models.TextField(blank=True, null=True)),
                ("length", models.TextField(blank=True, null=True)),
                ("max_atmosphering_speed", models.TextField(blank=True, null=True)),
                ("crew", models.TextField(blank=True, null=True)),
                ("passengers", models.TextField(blank=True, null=True)),
                ("cargo_capacity", models.TextField(blank=True, null=True)),
                ("consumables", models.TextField(blank=True, null=True)),
                ("vehicle_class", models.TextField(blank=True, null=True)),
                ("pilots", models.TextField(blank=True, null=True)),
                ("films", models.TextField(blank=True, null=True)),
                ("url", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "starwars_vehicles",
                "managed": False,
            },
        ),
    ]
