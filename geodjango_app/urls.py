from django.conf.urls import patterns, url
from geodjango_app import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='geodjango_app-index'),
    )
