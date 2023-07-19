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


class WeeklyBoxOffice(models.Model):
    index = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField(
        db_column="Date", blank=True, null=True
    )  # Field name made lowercase.
    gross = models.BigIntegerField(
        db_column="Gross", blank=True, null=True
    )  # Field name made lowercase.
    theaters = models.BigIntegerField(
        db_column="Theaters", blank=True, null=True
    )  # Field name made lowercase.
    per_theater = models.BigIntegerField(
        db_column="Per Theater", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_gross = models.BigIntegerField(
        db_column="Total Gross", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    week = models.BigIntegerField(
        db_column="Week", blank=True, null=True
    )  # Field name made lowercase.
    movie = models.TextField(
        db_column="Movie", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "weekly_box_office"


class Starwarsbudgetandprofit(models.Model):
    index = models.BigIntegerField(primary_key=True)
    release_date = models.TextField(
        db_column="Release Date", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    title = models.TextField(
        db_column="Title", blank=True, null=True
    )  # Field name made lowercase.
    production_budget = models.TextField(
        db_column="Production Budget", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    opening_weekend = models.TextField(
        db_column="Opening Weekend", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    domestic_box_office = models.TextField(
        db_column="Domestic Box Office", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    worldwide_box_office = models.TextField(
        db_column="Worldwide Box Office", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "StarwarsBudgetAndProfit"
class Swcscreentime(models.Model):
    index = models.BigIntegerField(primary_key=True)
    movie = models.TextField(db_column='Movie', blank=True, null=True)  # Field name made lowercase.
    character = models.TextField(db_column='Character', blank=True, null=True)  # Field name made lowercase.
    length_of_movie = models.TextField(db_column='Length of Movie', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    character_screentime = models.TextField(db_column='Character Screentime', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    percentage = models.TextField(db_column='Percentage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SWCScreentime'
        
class StarwarsCrawlers(models.Model):
    index = models.BigIntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    trailer = models.TextField(blank=True, null=True)
    crawl = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'starwars_crawlers'