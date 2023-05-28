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

