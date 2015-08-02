from django.contrib.gis.db import models


class HebridesCycle(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    cmt = models.CharField(max_length=254, blank=True, null=True)
    desc = models.CharField(max_length=254, blank=True, null=True)
    src = models.CharField(max_length=254, blank=True, null=True)
    link1_href = models.CharField(max_length=254, blank=True, null=True)
    link1_text = models.CharField(max_length=254, blank=True, null=True)
    link1_type = models.CharField(max_length=254, blank=True, null=True)
    link2_href = models.CharField(max_length=254, blank=True, null=True)
    link2_text = models.CharField(max_length=254, blank=True, null=True)
    link2_type = models.CharField(max_length=254, blank=True, null=True)
    number = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    type = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiLineStringField(srid=27700)
    objects = models.GeoManager()