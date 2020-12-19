from django.conf.urls import url
from . import views as core_views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^signin/$', core_views.signin, name='signin'),
    url(r'^logout/$', core_views.logout, name='logout'),
    url(r'^edit/$', core_views.edit, name='edit'),
    

]