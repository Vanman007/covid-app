from django.conf.urls import url
from . import views as core_views

app_name = 'search'

urlpatterns = [
    url(r'^search/$', core_views.search, name='search'),


]