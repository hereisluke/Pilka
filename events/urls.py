from django.conf.urls import url

from . import views

app_name = 'events'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/event/$', views.EventView.as_view(), name='event'),
    url(r'^(?P<pk>[0-9]+)/place/$', views.PlaceView.as_view(), name='place'),
]
