from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^add/quantity$', views.add_quantity, name='add_quantity'),
)