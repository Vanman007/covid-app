from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django_elasticsearch_dsl_drf.wrappers import dict_to_obj

User = get_user_model()

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=150)
    covid_info = models.CharField(max_length=200)
    latitude = models.DecimalField(null=True,
                               blank=True,
                               decimal_places=15,
                               max_digits=19,
                               default=0)
    longitude = models.DecimalField(null=True,
                                    blank=True,
                                    decimal_places=15,
                                    max_digits=19,
                                    default=0)

 #   user = models.OneToOneField(User, related_name='search', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        #app_label = 'search'

    @property
    def location_field_indexing(self):
        """Location for indexing.

        Used in Elasticsearch indexing/tests of `geo_distance` native filter.
        """
        return {
            'lat': self.latitude,
            'lon': self.longitude,
        }


class City(models.Model):
    name=models.CharField(max_length=150)
    covid_info = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    latitude = models.DecimalField(null=True,
                               blank=True,
                               decimal_places=15,
                               max_digits=19,
                               default=0)
    longitude = models.DecimalField(null=True,
                                    blank=True,
                                    decimal_places=15,
                                    max_digits=19,
                                    default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]

    @property
    def location_field_indexing(self):
        """Location for indexing.

        Used in Elasticsearch indexing/tests of `geo_distance` native filter.
        """
        return {
            'lat': self.latitude,
            'lon': self.longitude,
        }

class CovidUser(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    has_covid = models.BooleanField(default=True)
    user = models.OneToOneField(User, related_name='search', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["id"]


    @property
    def country_indexing(self):
        wrapper = dict_to_obj({
            'name': self.city.country.name,
            'city': {
                'name': self.city.name
            }
        })

        return wrapper

