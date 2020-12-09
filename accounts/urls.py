from django.conf.urls import url
from . import views as core_views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),


]