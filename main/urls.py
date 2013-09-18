from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^add/quantity$', views.add_quantity, name='add_quantity'),
    url(r'^object/(?P<object_name>.+)/$', views.object_view, name='object_view'),
    url(r'^definition/(?P<definition_name>.+)/$', views.definition_view, name='definition_view'),
    url(r'^object_list/$', views.object_list, name='object_list'),
)