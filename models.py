#from__future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = GeoManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Incidences'

class IND_adm1(models.Model):
    id_1 = models.BigIntegerField()
    name_1 = models.CharField(max_length=75)
    type_1 = models.CharField(max_length=50)
    engtype_1 = models.CharField(max_length=50)
    nl_name_1 = models.CharField(max_length=50)
    varname_1 = models.CharField(max_length=150)
    id_0 = models.BigIntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name_1


class newwater(models.Model):
    serial = models.BigIntegerField()
    field_2 = models.BigIntegerField()
    field_3 = models.BigIntegerField()
    field_4 = models.CharField(max_length=254)
    district = models.CharField(max_length=254)
    town = models.CharField(max_length=254)
    area = models.CharField(max_length=254)
    lat = models.CharField(max_length=254)
    lon = models.CharField(max_length=254)
    x = models.FloatField()
    y = models.FloatField()
    pre_1 = models.CharField(max_length=254)
    pre_2 = models.BigIntegerField()
    pre_3 = models.FloatField()
    pre_4 = models.FloatField()
    pre_5 = models.FloatField()
    pre_6 = models.FloatField()
    pre_7 = models.FloatField()
    pre_8 = models.FloatField()
    pre_9 = models.FloatField()
    pre_10 = models.FloatField()

    pre_11 = models.FloatField()
    pre_12 = models.FloatField()
    pre_13 = models.FloatField()
    pre_14 = models.FloatField()
    pre_15 = models.FloatField()
    pre_16 = models.CharField(max_length=254)
    pre_17 = models.FloatField()
    pre_18 = models.FloatField()
    pre_19 = models.FloatField()
    pre_20 = models.FloatField()
    pre_21 = models.FloatField()
    pre_22 = models.FloatField()
    pre_23 = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)
    objects = GeoManager()

    def __str__(self):
        return self.town

