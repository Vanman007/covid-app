from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .api_views import CovidUserDocumentView



router = DefaultRouter()

router.register(
    r'search',
    CovidUserDocumentView,
    basename='searchdocument'
)

urlpatterns = [
   # path('manage-covid-user/', views.CovidUser.as_view()),
   # path('manage-user/', views.CurrentUserUser.as_view()),
    url(r'^', include(router.urls)),
]
