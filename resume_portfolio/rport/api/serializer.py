from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


# Serializers define the API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class StudentPerformanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.StudentPerformance
        fields = [
            "gender",
            "race_ethnicity",
            "parental_level_of_education",
            "lunch",
            "test_preparation_course",
            "math_score",
            "reading_score",
            "writing_score",
        ]


class SqlExamplesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SqlExamples
        fields = [
            "index",
            "difficulty",
            "question",
            "solution",
            "comments",
        ]


class AnimalCrossingNewHorizonCatalogAccessoriesSerializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogAccessories
        fields = [
            "index",
            "name",
            "variation",
            "diy",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "miles_price",
            "source",
            "source_notes",
            "seasonal_availability",
            "mannequin_piece",
            "version",
            "style",
            "label_themes",
            "type",
            "villager_equippable",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogAchievementsSerializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogAchievements
        fields = [
            "index",
            "name",
            "award_criteria",
            "field_field",
            "internal_id",
            "internal_name",
            "internal_category",
            "num_of_tiers",
            "tier_1",
            "tier_2",
            "tier_3",
            "tier_4",
            "tier_5",
            "reward_tier_1",
            "reward_tier_2",
            "reward_tier_3",
            "reward_tier_4",
            "reward_tier_5",
            "reward_tier_6",
            "sequential",
            "version",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogArtSerializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogArt
        fields = [
            "index",
            "name",
            "genuine",
            "category",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "real_artwork_title",
            "artist",
            "museum_description",
            "source",
            "source_notes",
            "version",
            "hha_concept_1",
            "hha_concept_2",
            "hha_series",
            "hha_set",
            "interact",
            "tag",
            "speaker_type",
            "lighting_type",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogBagsSerializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogBags
        fields = [
            "index",
            "name",
            "variation",
            "diy",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "miles_price",
            "source",
            "source_notes",
            "seasonal_availability",
            "version",
            "style",
            "label_themes",
            "villager_equippable",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogBottomsSerializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogBottoms
        fields = [
            "index",
            "name",
            "variation",
            "diy",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "source",
            "source_notes",
            "seasonal_availability",
            "mannequin_piece",
            "version",
            "style",
            "label_themes",
            "villager_equippable",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogConstructionSerializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogConstruction
        fields = [
            "index",
            "name",
            "buy",
            "category",
            "source",
            "filename",
            "version",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogDressUpSerializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogDressUp
        fields = [
            "index",
            "name",
            "variation",
            "diy",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "source",
            "source_notes",
            "seasonal_availability",
            "mannequin_piece",
            "version",
            "style",
            "label_themes",
            "villager_equippable",
            "catalog",
            "primary_shape",
            "secondary_shape",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


# ----------------------------------------------------------------
class AnimalCrossingNewHorizonCatalogFencingSerializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogFencing
        fields = [
            "index",
            "name",
            "diy",
            "stack_size",
            "buy",
            "sell",
            "source",
            "source_notes",
            "version",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogFishSerializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogFish
        fields = [
            "index",
            "field_field",
            "name",
            "sell",
            "where_how",
            "shadow",
            "total_catches_to_unlock",
            "spawn_rates",
            "rain_snow_catch_up",
            "nh_jan",
            "nh_feb",
            "nh_mar",
            "nh_apr",
            "nh_may",
            "nh_jun",
            "nh_jul",
            "nh_aug",
            "nh_sep",
            "nh_oct",
            "nh_nov",
            "nh_dec",
            "sh_jan",
            "sh_feb",
            "sh_mar",
            "sh_apr",
            "sh_may",
            "sh_jun",
            "sh_jul",
            "sh_aug",
            "sh_sep",
            "sh_oct",
            "sh_nov",
            "sh_dec",
            "color_1",
            "color_2",
            "size",
            "lighting_type",
            "icon_filename",
            "critterpedia_filename",
            "furniture_filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogFloorsSerializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogFloors
        fields = [
            "index",
            "name",
            "vfx",
            "diy",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "miles_price",
            "source",
            "source_notes",
            "version",
            "hha_concept_1",
            "hha_concept_2",
            "hha_series",
            "tag",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogFossilsserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogFossils
        fields = [
            "index",
            "name",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "source",
            "museum",
            "version",
            "interact",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogHeadwearserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogHeadwear
        fields = [
            "index",
            "name",
            "variation",
            "diy",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "miles_price",
            "source",
            "source_notes",
            "seasonal_availability",
            "mannequin_piece",
            "version",
            "style",
            "label_themes",
            "type",
            "villager_equippable",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogHousewaresserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogHousewares
        fields = [
            "index",
            "name",
            "variation",
            "body_title",
            "pattern",
            "pattern_title",
            "diy",
            "body_customize",
            "pattern_customize",
            "kit_cost",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "miles_price",
            "source",
            "source_notes",
            "version",
            "hha_concept_1",
            "hha_concept_2",
            "hha_series",
            "hha_set",
            "interact",
            "tag",
            "outdoor",
            "speaker_type",
            "lighting_type",
            "catalog",
            "filename",
            "variant_id",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogInsectsserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogInsects
        fields = [
            "index",
            "field_field",
            "name",
            "sell",
            "where_how",
            "weather",
            "total_catches_to_unlock",
            "spawn_rates",
            "nh_jan",
            "nh_feb",
            "nh_mar",
            "nh_apr",
            "nh_may",
            "nh_jun",
            "nh_jul",
            "nh_aug",
            "nh_sep",
            "nh_oct",
            "nh_nov",
            "nh_dec",
            "sh_jan",
            "sh_feb",
            "sh_mar",
            "sh_apr",
            "sh_may",
            "sh_jun",
            "sh_jul",
            "sh_aug",
            "sh_sep",
            "sh_oct",
            "sh_nov",
            "sh_dec",
            "color_1",
            "color_2",
            "icon_filename",
            "critterpedia_filename",
            "furniture_filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogMiscellaneousserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogMiscellaneous
        fields = [
            "index",
            "name",
            "variation",
            "body_title",
            "pattern",
            "pattern_title",
            "diy",
            "body_customize",
            "pattern_customize",
            "kit_cost",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "source",
            "source_notes",
            "version",
            "hha_concept_1",
            "hha_concept_2",
            "hha_series",
            "hha_set",
            "interact",
            "tag",
            "outdoor",
            "speaker_type",
            "lighting_type",
            "catalog",
            "filename",
            "variant_id",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogMusicserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogMusic
        fields = [
            "index",
            "name",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "source",
            "source_notes",
            "version",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogOtherserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogOther
        fields = [
            "index",
            "name",
            "diy",
            "stack_size",
            "buy",
            "sell",
            "miles_price",
            "source",
            "source_notes",
            "tag",
            "color_1",
            "color_2",
            "version",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogPhotosserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogPhotos
        fields = [
            "index",
            "name",
            "variation",
            "body_title",
            "pattern",
            "pattern_title",
            "diy",
            "customize",
            "kit_cost",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "source",
            "version",
            "catalog",
            "filename",
            "variant_id",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogPostersserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogPosters
        fields = [
            "name",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "source",
            "source_notes",
            "version",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogReactionsserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogReactions
        fields = [
            "index",
            "name",
            "source",
            "source_notes",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogRecipesserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogRecipes
        fields = [
            "index",
            "name",
            "field_1",
            "material_1",
            "field_2",
            "material_2",
            "field_3",
            "material_3",
            "field_4",
            "material_4",
            "field_5",
            "material_5",
            "field_6",
            "material_6",
            "buy",
            "sell",
            "miles_price",
            "source",
            "source_notes",
            "recipes_to_unlock",
            "version",
            "category",
            "serial_id",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogRugsserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogRugs
        fields = [
            "index",
            "name",
            "diy",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "miles_price",
            "source",
            "source_notes",
            "version",
            "hha_concept_1",
            "hha_concept_2",
            "hha_series",
            "tag",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogShoesserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogShoes
        fields = [
            "index",
            "name",
            "variation",
            "diy",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "miles_price",
            "source",
            "source_notes",
            "seasonal_availability",
            "mannequin_piece",
            "version",
            "style",
            "label_themes",
            "villager_equippable",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogSocksserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogSocks
        fields = [
            "index",
            "name",
            "variation",
            "diy",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "miles_price",
            "source",
            "source_notes",
            "seasonal_availability",
            "mannequin_piece",
            "version",
            "style",
            "label_themes",
            "villager_equippable",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogToolsserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogTools
        fields = [
            "index",
            "name",
            "variation",
            "body_title",
            "diy",
            "customize",
            "kit_cost",
            "uses",
            "stack_size",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "set",
            "miles_price",
            "source",
            "source_notes",
            "version",
            "filename",
            "variant_id",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogTopsserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogTops
        fields = [
            "index",
            "name",
            "variation",
            "diy",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "miles_price",
            "source",
            "source_notes",
            "seasonal_availability",
            "mannequin_piece",
            "version",
            "style",
            "label_themes",
            "villager_equippable",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogUmbrellasserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogUmbrellas
        fields = [
            "index",
            "name",
            "diy",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "miles_price",
            "source",
            "source_notes",
            "version",
            "villager_equippable",
            "catalog",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogVillagersserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogVillagers
        fields = [
            "index",
            "name",
            "species",
            "gender",
            "personality",
            "hobby",
            "birthday",
            "catchphrase",
            "favorite_song",
            "style_1",
            "style_2",
            "color_1",
            "color_2",
            "wallpaper",
            "flooring",
            "furniture_list",
            "filename",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogWallMountedserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogWallMounted
        fields = [
            "index",
            "name",
            "variation",
            "body_title",
            "pattern",
            "pattern_title",
            "diy",
            "body_customize",
            "pattern_customize",
            "kit_cost",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "size",
            "source",
            "source_notes",
            "version",
            "hha_concept_1",
            "hha_concept_2",
            "hha_series",
            "hha_set",
            "interact",
            "tag",
            "outdoor",
            "lighting_type",
            "door_deco",
            "catalog",
            "filename",
            "variant_id",
            "internal_id",
            "unique_entry_id",
        ]


class AnimalCrossingNewHorizonCatalogWallpaperserializer(
    serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.AnimalCrossingNewHorizonCatalogWallpaper
        fields = [
            "index",
            "name",
            "vfx",
            "vfx_type",
            "diy",
            "buy",
            "sell",
            "color_1",
            "color_2",
            "miles_price",
            "source",
            "source_notes",
            "catalog",
            "window_type",
            "window_color",
            "pane_type",
            "curtain_type",
            "curtain_color",
            "ceiling_type",
            "hha_concept_1",
            "hha_concept_2",
            "hha_series",
            "tag",
            "version",
            "filename",
            "internal_id",
            "unique_entry_id",
        ]


class NetflixTitlesserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.NetflixTitles
        fields = [
            "index",
            "show_id",
            "type",
            "title",
            "director",
            "cast",
            "country",
            "date_added",
            "release_year",
            "rating",
            "duration",
            "listed_in",
            "description",
        ]
