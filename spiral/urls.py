from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.people_list, name='people_list'),
]
