from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

User = get_user_model()

# Create your models here.
class CovidUser(models.Model):
    city=models.CharField(max_length=150)
    country=models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    hasCovid = models.BooleanField(default=True)

    user = models.ForeignKey(User, related_name='search', on_delete=models.CASCADE)

    def __str__(self):
        return self.country

    class Meta:
        app_label = 'search'