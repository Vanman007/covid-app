from django.contrib import admin

# Register your models here.

from search.models import CovidUser, City, Country

admin.site.register(CovidUser)
admin.site.register(City)
admin.site.register(Country)
