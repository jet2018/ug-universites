from django.contrib.gis.db.models import PointField
from django.db import models


class University(models.Model):
    '''A Univesity with a name and location'''
    univerity_name = models.CharField(max_length=255)
    univerity_location = PointField()


class TestUniversity(models.Model):
    '''A University with a name and location'''
    university_name = models.CharField(max_length=200)
    university_location = PointField()

    class Meta:
        verbose_name = 'Test Universities'
