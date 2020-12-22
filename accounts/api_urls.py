from django.conf.urls import url, include
from django.urls import path
from . import api_views as views 

urlpatterns = [
    url('google_auth', views.GoogleAuth.as_view() , name="google-auth"),
]
