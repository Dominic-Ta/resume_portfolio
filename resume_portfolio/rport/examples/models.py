from django.db import models


class NetflixTitles(models.Model):
    index = models.BigIntegerField(primary_key=True)
    show_id = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    date_added = models.TextField(blank=True, null=True)
    release_year = models.BigIntegerField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    listed_in = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "netflix_titles"

class CharacterData(models.Model):
    index = models.TextField(primary_key=True)
    height = models.TextField(blank=True, null=True)
    mass = models.TextField(blank=True, null=True)
    skin_color = models.TextField(blank=True, null=True)
    hair_color = models.TextField(blank=True, null=True)
    birth_year = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    homeworld = models.TextField(blank=True, null=True)
    films = models.TextField(blank=True, null=True)
    species = models.TextField(blank=True, null=True)
    char_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "character_data"


class StarwarsFilms(models.Model):
    index = models.BigIntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    episode_id = models.BigIntegerField(blank=True, null=True)
    opening_crawl = models.TextField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    producer = models.TextField(blank=True, null=True)
    release_date = models.TextField(blank=True, null=True)
    characters = models.TextField(blank=True, null=True)
    planets = models.TextField(blank=True, null=True)
    starships = models.TextField(blank=True, null=True)
    vehicles = models.TextField(blank=True, null=True)
    species = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "starwars_films"


class StarwarsPlanets(models.Model):
    index = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    rotation_period = models.TextField(blank=True, null=True)
    orbital_period = models.TextField(blank=True, null=True)
    diameter = models.TextField(blank=True, null=True)
    climate = models.TextField(blank=True, null=True)
    gravity = models.TextField(blank=True, null=True)
    terrain = models.TextField(blank=True, null=True)
    surface_water = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    residents = models.TextField(blank=True, null=True)
    films = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "starwars_planets"


class StarwarsSpecies(models.Model):
    index = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    classification = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)
    average_height = models.TextField(blank=True, null=True)
    skin_colors = models.TextField(blank=True, null=True)
    hair_colors = models.TextField(blank=True, null=True)
    eye_colors = models.TextField(blank=True, null=True)
    average_lifespan = models.TextField(blank=True, null=True)
    homeworld = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    people = models.TextField(blank=True, null=True)
    films = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "starwars_species"


class StarwarsStarships(models.Model):
    index = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    manufacturer = models.TextField(blank=True, null=True)
    cost_in_credits = models.TextField(blank=True, null=True)
    length = models.TextField(blank=True, null=True)
    max_atmosphering_speed = models.TextField(blank=True, null=True)
    crew = models.TextField(blank=True, null=True)
    passengers = models.TextField(blank=True, null=True)
    cargo_capacity = models.TextField(blank=True, null=True)
    consumables = models.TextField(blank=True, null=True)
    hyperdrive_rating = models.TextField(blank=True, null=True)
    mglt = models.TextField(
        db_column="MGLT", blank=True, null=True
    )  # Field name made lowercase.
    starship_class = models.TextField(blank=True, null=True)
    pilots = models.TextField(blank=True, null=True)
    films = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "starwars_starships"


class StarwarsVehicles(models.Model):
    index = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    manufacturer = models.TextField(blank=True, null=True)
    cost_in_credits = models.TextField(blank=True, null=True)
    length = models.TextField(blank=True, null=True)
    max_atmosphering_speed = models.TextField(blank=True, null=True)
    crew = models.TextField(blank=True, null=True)
    passengers = models.TextField(blank=True, null=True)
    cargo_capacity = models.TextField(blank=True, null=True)
    consumables = models.TextField(blank=True, null=True)
    vehicle_class = models.TextField(blank=True, null=True)
    pilots = models.TextField(blank=True, null=True)
    films = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "starwars_vehicles"
