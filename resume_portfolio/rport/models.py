# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Swcscreentime(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    movie = models.TextField(db_column='Movie', blank=True, null=True)  # Field name made lowercase.
    character = models.TextField(db_column='Character', blank=True, null=True)  # Field name made lowercase.
    length_of_movie = models.TextField(db_column='Length of Movie', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    character_screentime = models.TextField(db_column='Character Screentime', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    percentage = models.TextField(db_column='Percentage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SWCScreentime'


class Starwarsbudgetandprofit(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    release_date = models.TextField(db_column='Release Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    production_budget = models.TextField(db_column='Production Budget', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    opening_weekend = models.TextField(db_column='Opening Weekend', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    domestic_box_office = models.TextField(db_column='Domestic Box Office', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    worldwide_box_office = models.TextField(db_column='Worldwide Box Office', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'StarwarsBudgetAndProfit'


class AnimalCrossingNewHorizonCatalogAccessories(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    variation = models.TextField(db_column='Variation', blank=True, null=True)  # Field name made lowercase.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seasonal_availability = models.TextField(db_column='Seasonal Availability', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mannequin_piece = models.TextField(db_column='Mannequin Piece', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    style = models.TextField(db_column='Style', blank=True, null=True)  # Field name made lowercase.
    label_themes = models.TextField(db_column='Label Themes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    villager_equippable = models.TextField(db_column='Villager Equippable', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_accessories'


class AnimalCrossingNewHorizonCatalogAchievements(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    award_criteria = models.TextField(db_column='Award Criteria', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_field = models.BigIntegerField(db_column='#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_name = models.TextField(db_column='Internal Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_category = models.TextField(db_column='Internal Category', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    num_of_tiers = models.BigIntegerField(db_column='Num of Tiers', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tier_1 = models.BigIntegerField(db_column='Tier 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tier_2 = models.BigIntegerField(db_column='Tier 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tier_3 = models.BigIntegerField(db_column='Tier 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tier_4 = models.BigIntegerField(db_column='Tier 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tier_5 = models.BigIntegerField(db_column='Tier 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reward_tier_1 = models.BigIntegerField(db_column='Reward Tier 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reward_tier_2 = models.BigIntegerField(db_column='Reward Tier 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reward_tier_3 = models.BigIntegerField(db_column='Reward Tier 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reward_tier_4 = models.BigIntegerField(db_column='Reward Tier 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reward_tier_5 = models.BigIntegerField(db_column='Reward Tier 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reward_tier_6 = models.BigIntegerField(db_column='Reward Tier 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sequential = models.TextField(db_column='Sequential', blank=True, null=True)  # Field name made lowercase.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_achievements'


class AnimalCrossingNewHorizonCatalogArt(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    genuine = models.TextField(db_column='Genuine', blank=True, null=True)  # Field name made lowercase.
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    buy = models.BigIntegerField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    real_artwork_title = models.TextField(db_column='Real Artwork Title', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    artist = models.TextField(db_column='Artist', blank=True, null=True)  # Field name made lowercase.
    museum_description = models.TextField(db_column='Museum Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    hha_concept_1 = models.TextField(db_column='HHA Concept 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_concept_2 = models.TextField(db_column='HHA Concept 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_series = models.TextField(db_column='HHA Series', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    hha_set = models.TextField(db_column='HHA Set', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    interact = models.TextField(db_column='Interact', blank=True, null=True)  # Field name made lowercase.
    tag = models.TextField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    speaker_type = models.TextField(db_column='Speaker Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lighting_type = models.TextField(db_column='Lighting Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_art'


class AnimalCrossingNewHorizonCatalogBags(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    variation = models.TextField(db_column='Variation', blank=True, null=True)  # Field name made lowercase.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seasonal_availability = models.TextField(db_column='Seasonal Availability', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    style = models.TextField(db_column='Style', blank=True, null=True)  # Field name made lowercase.
    label_themes = models.TextField(db_column='Label Themes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    villager_equippable = models.TextField(db_column='Villager Equippable', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_bags'


class AnimalCrossingNewHorizonCatalogBottoms(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    variation = models.TextField(db_column='Variation', blank=True, null=True)  # Field name made lowercase.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seasonal_availability = models.TextField(db_column='Seasonal Availability', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mannequin_piece = models.TextField(db_column='Mannequin Piece', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    style = models.TextField(db_column='Style', blank=True, null=True)  # Field name made lowercase.
    label_themes = models.TextField(db_column='Label Themes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    villager_equippable = models.TextField(db_column='Villager Equippable', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_bottoms'


class AnimalCrossingNewHorizonCatalogConstruction(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    buy = models.BigIntegerField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_construction'


class AnimalCrossingNewHorizonCatalogDressUp(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    variation = models.TextField(db_column='Variation', blank=True, null=True)  # Field name made lowercase.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seasonal_availability = models.TextField(db_column='Seasonal Availability', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mannequin_piece = models.TextField(db_column='Mannequin Piece', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    style = models.TextField(db_column='Style', blank=True, null=True)  # Field name made lowercase.
    label_themes = models.TextField(db_column='Label Themes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    villager_equippable = models.TextField(db_column='Villager Equippable', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    primary_shape = models.TextField(db_column='Primary Shape', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    secondary_shape = models.TextField(db_column='Secondary Shape', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_dress-up'


class AnimalCrossingNewHorizonCatalogFencing(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    stack_size = models.BigIntegerField(db_column='Stack Size', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_fencing'


class AnimalCrossingNewHorizonCatalogFish(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    field_field = models.BigIntegerField(db_column='#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    where_how = models.TextField(db_column='Where/How', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shadow = models.TextField(db_column='Shadow', blank=True, null=True)  # Field name made lowercase.
    total_catches_to_unlock = models.BigIntegerField(db_column='Total Catches to Unlock', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    spawn_rates = models.TextField(db_column='Spawn Rates', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rain_snow_catch_up = models.TextField(db_column='Rain/Snow Catch Up', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_jan = models.TextField(db_column='NH Jan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_feb = models.TextField(db_column='NH Feb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_mar = models.TextField(db_column='NH Mar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_apr = models.TextField(db_column='NH Apr', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_may = models.TextField(db_column='NH May', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_jun = models.TextField(db_column='NH Jun', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_jul = models.TextField(db_column='NH Jul', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_aug = models.TextField(db_column='NH Aug', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_sep = models.TextField(db_column='NH Sep', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_oct = models.TextField(db_column='NH Oct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_nov = models.TextField(db_column='NH Nov', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_dec = models.TextField(db_column='NH Dec', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_jan = models.TextField(db_column='SH Jan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_feb = models.TextField(db_column='SH Feb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_mar = models.TextField(db_column='SH Mar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_apr = models.TextField(db_column='SH Apr', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_may = models.TextField(db_column='SH May', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_jun = models.TextField(db_column='SH Jun', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_jul = models.TextField(db_column='SH Jul', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_aug = models.TextField(db_column='SH Aug', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_sep = models.TextField(db_column='SH Sep', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_oct = models.TextField(db_column='SH Oct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_nov = models.TextField(db_column='SH Nov', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_dec = models.TextField(db_column='SH Dec', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    lighting_type = models.TextField(db_column='Lighting Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    icon_filename = models.TextField(db_column='Icon Filename', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    critterpedia_filename = models.TextField(db_column='Critterpedia Filename', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    furniture_filename = models.TextField(db_column='Furniture Filename', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_fish'


class AnimalCrossingNewHorizonCatalogFloors(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    vfx = models.TextField(db_column='VFX', blank=True, null=True)  # Field name made lowercase.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    hha_concept_1 = models.TextField(db_column='HHA Concept 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_concept_2 = models.TextField(db_column='HHA Concept 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_series = models.TextField(db_column='HHA Series', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tag = models.TextField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_floors'


class AnimalCrossingNewHorizonCatalogFossils(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    museum = models.TextField(db_column='Museum', blank=True, null=True)  # Field name made lowercase.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    interact = models.TextField(db_column='Interact', blank=True, null=True)  # Field name made lowercase.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_fossils'


class AnimalCrossingNewHorizonCatalogHeadwear(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    variation = models.TextField(db_column='Variation', blank=True, null=True)  # Field name made lowercase.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seasonal_availability = models.TextField(db_column='Seasonal Availability', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mannequin_piece = models.TextField(db_column='Mannequin Piece', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    style = models.TextField(db_column='Style', blank=True, null=True)  # Field name made lowercase.
    label_themes = models.TextField(db_column='Label Themes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    villager_equippable = models.TextField(db_column='Villager Equippable', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_headwear'


class AnimalCrossingNewHorizonCatalogHousewares(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    variation = models.TextField(db_column='Variation', blank=True, null=True)  # Field name made lowercase.
    body_title = models.TextField(db_column='Body Title', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pattern = models.TextField(db_column='Pattern', blank=True, null=True)  # Field name made lowercase.
    pattern_title = models.TextField(db_column='Pattern Title', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    body_customize = models.TextField(db_column='Body Customize', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pattern_customize = models.TextField(db_column='Pattern Customize', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kit_cost = models.TextField(db_column='Kit Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    hha_concept_1 = models.TextField(db_column='HHA Concept 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_concept_2 = models.TextField(db_column='HHA Concept 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_series = models.TextField(db_column='HHA Series', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_set = models.TextField(db_column='HHA Set', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    interact = models.TextField(db_column='Interact', blank=True, null=True)  # Field name made lowercase.
    tag = models.TextField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    outdoor = models.TextField(db_column='Outdoor', blank=True, null=True)  # Field name made lowercase.
    speaker_type = models.TextField(db_column='Speaker Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lighting_type = models.TextField(db_column='Lighting Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    variant_id = models.TextField(db_column='Variant ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_housewares'


class AnimalCrossingNewHorizonCatalogInsects(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    field_field = models.BigIntegerField(db_column='#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    where_how = models.TextField(db_column='Where/How', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    weather = models.TextField(db_column='Weather', blank=True, null=True)  # Field name made lowercase.
    total_catches_to_unlock = models.BigIntegerField(db_column='Total Catches to Unlock', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    spawn_rates = models.TextField(db_column='Spawn Rates', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_jan = models.TextField(db_column='NH Jan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_feb = models.TextField(db_column='NH Feb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_mar = models.TextField(db_column='NH Mar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_apr = models.TextField(db_column='NH Apr', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_may = models.TextField(db_column='NH May', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_jun = models.TextField(db_column='NH Jun', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_jul = models.TextField(db_column='NH Jul', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_aug = models.TextField(db_column='NH Aug', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_sep = models.TextField(db_column='NH Sep', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_oct = models.TextField(db_column='NH Oct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_nov = models.TextField(db_column='NH Nov', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nh_dec = models.TextField(db_column='NH Dec', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_jan = models.TextField(db_column='SH Jan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_feb = models.TextField(db_column='SH Feb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_mar = models.TextField(db_column='SH Mar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_apr = models.TextField(db_column='SH Apr', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_may = models.TextField(db_column='SH May', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_jun = models.TextField(db_column='SH Jun', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_jul = models.TextField(db_column='SH Jul', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_aug = models.TextField(db_column='SH Aug', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_sep = models.TextField(db_column='SH Sep', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_oct = models.TextField(db_column='SH Oct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_nov = models.TextField(db_column='SH Nov', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sh_dec = models.TextField(db_column='SH Dec', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    icon_filename = models.TextField(db_column='Icon Filename', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    critterpedia_filename = models.TextField(db_column='Critterpedia Filename', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    furniture_filename = models.TextField(db_column='Furniture Filename', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_insects'


class AnimalCrossingNewHorizonCatalogMiscellaneous(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    variation = models.TextField(db_column='Variation', blank=True, null=True)  # Field name made lowercase.
    body_title = models.TextField(db_column='Body Title', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pattern = models.TextField(db_column='Pattern', blank=True, null=True)  # Field name made lowercase.
    pattern_title = models.TextField(db_column='Pattern Title', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    body_customize = models.TextField(db_column='Body Customize', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pattern_customize = models.TextField(db_column='Pattern Customize', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kit_cost = models.TextField(db_column='Kit Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    hha_concept_1 = models.TextField(db_column='HHA Concept 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_concept_2 = models.TextField(db_column='HHA Concept 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_series = models.TextField(db_column='HHA Series', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_set = models.TextField(db_column='HHA Set', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    interact = models.TextField(db_column='Interact', blank=True, null=True)  # Field name made lowercase.
    tag = models.TextField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    outdoor = models.TextField(db_column='Outdoor', blank=True, null=True)  # Field name made lowercase.
    speaker_type = models.TextField(db_column='Speaker Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lighting_type = models.TextField(db_column='Lighting Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    variant_id = models.TextField(db_column='Variant ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_miscellaneous'


class AnimalCrossingNewHorizonCatalogMusic(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_music'


class AnimalCrossingNewHorizonCatalogOther(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    stack_size = models.BigIntegerField(db_column='Stack Size', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.TextField(db_column='Sell', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tag = models.TextField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_other'


class AnimalCrossingNewHorizonCatalogPhotos(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    variation = models.TextField(db_column='Variation', blank=True, null=True)  # Field name made lowercase.
    body_title = models.TextField(db_column='Body Title', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pattern = models.TextField(db_column='Pattern', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pattern_title = models.TextField(db_column='Pattern Title', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    customize = models.TextField(db_column='Customize', blank=True, null=True)  # Field name made lowercase.
    kit_cost = models.BigIntegerField(db_column='Kit Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    variant_id = models.TextField(db_column='Variant ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_photos'


class AnimalCrossingNewHorizonCatalogPosters(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    buy = models.BigIntegerField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_posters'


class AnimalCrossingNewHorizonCatalogReactions(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_id = models.TextField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_reactions'


class AnimalCrossingNewHorizonCatalogRecipes(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    field_1 = models.BigIntegerField(db_column='#1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    material_1 = models.TextField(db_column='Material 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_2 = models.TextField(db_column='#2', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. This field type is a guess.
    material_2 = models.TextField(db_column='Material 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_3 = models.TextField(db_column='#3', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. This field type is a guess.
    material_3 = models.TextField(db_column='Material 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_4 = models.TextField(db_column='#4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. This field type is a guess.
    material_4 = models.TextField(db_column='Material 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_5 = models.TextField(db_column='#5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. This field type is a guess.
    material_5 = models.TextField(db_column='Material 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_6 = models.TextField(db_column='#6', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. This field type is a guess.
    material_6 = models.TextField(db_column='Material 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    recipes_to_unlock = models.BigIntegerField(db_column='Recipes to Unlock', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    serial_id = models.BigIntegerField(db_column='Serial ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_recipes'


class AnimalCrossingNewHorizonCatalogRugs(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    hha_concept_1 = models.TextField(db_column='HHA Concept 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_concept_2 = models.TextField(db_column='HHA Concept 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_series = models.TextField(db_column='HHA Series', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tag = models.TextField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_rugs'


class AnimalCrossingNewHorizonCatalogShoes(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    variation = models.TextField(db_column='Variation', blank=True, null=True)  # Field name made lowercase.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seasonal_availability = models.TextField(db_column='Seasonal Availability', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mannequin_piece = models.TextField(db_column='Mannequin Piece', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    style = models.TextField(db_column='Style', blank=True, null=True)  # Field name made lowercase.
    label_themes = models.TextField(db_column='Label Themes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    villager_equippable = models.TextField(db_column='Villager Equippable', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_shoes'


class AnimalCrossingNewHorizonCatalogSocks(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    variation = models.TextField(db_column='Variation', blank=True, null=True)  # Field name made lowercase.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seasonal_availability = models.TextField(db_column='Seasonal Availability', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mannequin_piece = models.TextField(db_column='Mannequin Piece', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    style = models.TextField(db_column='Style', blank=True, null=True)  # Field name made lowercase.
    label_themes = models.TextField(db_column='Label Themes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    villager_equippable = models.TextField(db_column='Villager Equippable', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_socks'


class AnimalCrossingNewHorizonCatalogTools(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    variation = models.TextField(db_column='Variation', blank=True, null=True)  # Field name made lowercase.
    body_title = models.TextField(db_column='Body Title', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    customize = models.TextField(db_column='Customize', blank=True, null=True)  # Field name made lowercase.
    kit_cost = models.TextField(db_column='Kit Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    uses = models.TextField(db_column='Uses', blank=True, null=True)  # Field name made lowercase.
    stack_size = models.BigIntegerField(db_column='Stack Size', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    set = models.TextField(db_column='Set', blank=True, null=True)  # Field name made lowercase.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    variant_id = models.TextField(db_column='Variant ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_tools'


class AnimalCrossingNewHorizonCatalogTops(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    variation = models.TextField(db_column='Variation', blank=True, null=True)  # Field name made lowercase.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seasonal_availability = models.TextField(db_column='Seasonal Availability', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mannequin_piece = models.TextField(db_column='Mannequin Piece', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    style = models.TextField(db_column='Style', blank=True, null=True)  # Field name made lowercase.
    label_themes = models.TextField(db_column='Label Themes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    villager_equippable = models.TextField(db_column='Villager Equippable', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_tops'


class AnimalCrossingNewHorizonCatalogUmbrellas(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.BigIntegerField(db_column='Sell', blank=True, null=True)  # Field name made lowercase.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    villager_equippable = models.TextField(db_column='Villager Equippable', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_umbrellas'


class AnimalCrossingNewHorizonCatalogVillagers(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    species = models.TextField(db_column='Species', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    personality = models.TextField(db_column='Personality', blank=True, null=True)  # Field name made lowercase.
    hobby = models.TextField(db_column='Hobby', blank=True, null=True)  # Field name made lowercase.
    birthday = models.TextField(db_column='Birthday', blank=True, null=True)  # Field name made lowercase.
    catchphrase = models.TextField(db_column='Catchphrase', blank=True, null=True)  # Field name made lowercase.
    favorite_song = models.TextField(db_column='Favorite Song', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    style_1 = models.TextField(db_column='Style 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    style_2 = models.TextField(db_column='Style 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wallpaper = models.TextField(db_column='Wallpaper', blank=True, null=True)  # Field name made lowercase.
    flooring = models.TextField(db_column='Flooring', blank=True, null=True)  # Field name made lowercase.
    furniture_list = models.TextField(db_column='Furniture List', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_villagers'


class AnimalCrossingNewHorizonCatalogWallMounted(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    variation = models.TextField(db_column='Variation', blank=True, null=True)  # Field name made lowercase.
    body_title = models.TextField(db_column='Body Title', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pattern = models.TextField(db_column='Pattern', blank=True, null=True)  # Field name made lowercase.
    pattern_title = models.TextField(db_column='Pattern Title', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    body_customize = models.TextField(db_column='Body Customize', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pattern_customize = models.TextField(db_column='Pattern Customize', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kit_cost = models.TextField(db_column='Kit Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.TextField(db_column='Sell', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    hha_concept_1 = models.TextField(db_column='HHA Concept 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_concept_2 = models.TextField(db_column='HHA Concept 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_series = models.TextField(db_column='HHA Series', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_set = models.TextField(db_column='HHA Set', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    interact = models.TextField(db_column='Interact', blank=True, null=True)  # Field name made lowercase.
    tag = models.TextField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    outdoor = models.TextField(db_column='Outdoor', blank=True, null=True)  # Field name made lowercase.
    lighting_type = models.TextField(db_column='Lighting Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    door_deco = models.TextField(db_column='Door Deco', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    variant_id = models.TextField(db_column='Variant ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_id = models.TextField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_wall-mounted'


class AnimalCrossingNewHorizonCatalogWallpaper(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    vfx = models.TextField(db_column='VFX', blank=True, null=True)  # Field name made lowercase.
    vfx_type = models.TextField(db_column='VFX Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diy = models.TextField(db_column='DIY', blank=True, null=True)  # Field name made lowercase.
    buy = models.TextField(db_column='Buy', blank=True, null=True)  # Field name made lowercase.
    sell = models.TextField(db_column='Sell', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    color_1 = models.TextField(db_column='Color 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_2 = models.TextField(db_column='Color 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    miles_price = models.TextField(db_column='Miles Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    source_notes = models.TextField(db_column='Source Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    catalog = models.TextField(db_column='Catalog', blank=True, null=True)  # Field name made lowercase.
    window_type = models.TextField(db_column='Window Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    window_color = models.TextField(db_column='Window Color', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pane_type = models.TextField(db_column='Pane Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    curtain_type = models.TextField(db_column='Curtain Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    curtain_color = models.TextField(db_column='Curtain Color', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ceiling_type = models.TextField(db_column='Ceiling Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_concept_1 = models.TextField(db_column='HHA Concept 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_concept_2 = models.TextField(db_column='HHA Concept 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hha_series = models.TextField(db_column='HHA Series', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tag = models.TextField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    internal_id = models.BigIntegerField(db_column='Internal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unique_entry_id = models.TextField(db_column='Unique Entry ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'animal_crossing_new_horizon_catalog_wallpaper'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CharacterData(models.Model):
    index = models.TextField(blank=True, null=True)
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
        db_table = 'character_data'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCache(models.Model):
    cache_key = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()
    expires = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_cache'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class NetflixTitles(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
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
        db_table = 'netflix_titles'


class SqlExamples(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    difficulty = models.TextField(db_column='Difficulty', blank=True, null=True)  # Field name made lowercase.
    question = models.TextField(db_column='Question', blank=True, null=True)  # Field name made lowercase.
    solution = models.TextField(db_column='Solution', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sql_examples'


class StarwarsCrawlers(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    trailer = models.TextField(blank=True, null=True)
    crawl = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'starwars_crawlers'


class StarwarsFilms(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
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
        db_table = 'starwars_films'


class StarwarsPlanets(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
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
        db_table = 'starwars_planets'


class StarwarsSpecies(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
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
        db_table = 'starwars_species'


class StarwarsStarships(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
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
    mglt = models.TextField(db_column='MGLT', blank=True, null=True)  # Field name made lowercase.
    starship_class = models.TextField(blank=True, null=True)
    pilots = models.TextField(blank=True, null=True)
    films = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'starwars_starships'


class StarwarsVehicles(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
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
        db_table = 'starwars_vehicles'


class StudentPerformance(models.Model):
    gender = models.TextField(blank=True, null=True)
    race_ethnicity = models.TextField(db_column='race/ethnicity', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    parental_level_of_education = models.TextField(db_column='parental level of education', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lunch = models.TextField(blank=True, null=True)
    test_preparation_course = models.TextField(db_column='test preparation course', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    math_score = models.TextField(db_column='math score', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    reading_score = models.TextField(db_column='reading score', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    writing_score = models.TextField(db_column='writing score', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'student_performance'


class WeeklyBoxOffice(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    gross = models.BigIntegerField(db_column='Gross', blank=True, null=True)  # Field name made lowercase.
    theaters = models.BigIntegerField(db_column='Theaters', blank=True, null=True)  # Field name made lowercase.
    per_theater = models.BigIntegerField(db_column='Per Theater', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_gross = models.BigIntegerField(db_column='Total Gross', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    week = models.BigIntegerField(db_column='Week', blank=True, null=True)  # Field name made lowercase.
    movie = models.TextField(db_column='Movie', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'weekly_box_office'
