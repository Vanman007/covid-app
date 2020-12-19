from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

User = get_user_model()

# Create your models here.
class CovidUser(models.Model):
    city=models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    country=models.CharField(max_length=150)
    state_province = models.CharField(max_length=80)
    created_at = models.DateTimeField(default=timezone.now)
    has_covid = models.BooleanField(default=True)
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

    user = models.OneToOneField(User, related_name='search', on_delete=models.CASCADE)

    def __str__(self):
        return self.country

    class Meta:
        app_label = 'search'

    @property
    def location_field_indexing(self):
        """Location for indexing.

        Used in Elasticsearch indexing/tests of `geo_distance` native filter.
        """
        return {
            'lat': self.latitude,
            'lon': self.longitude,
        }