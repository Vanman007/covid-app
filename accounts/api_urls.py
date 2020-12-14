from django.conf.urls import url
from django.urls import path

from . import api_views as views


urlpatterns = [
    path('manage-covid-user/', views.ManageCovidUser.as_view()),

]
