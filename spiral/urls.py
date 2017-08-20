from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.persons_list, name='persons_list'),
]
