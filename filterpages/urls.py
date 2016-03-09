from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^overview/(?P<year>[0-9]+)/(?P<make>[a-z]+[-.]?[a-z]+)/(?P<model>[0-9a-z]+[-.]?[0-9a-z]+)/(?P<body>[0-9a-z]+[-.]?[0-9a-z]+)/$', views.overview, name='overview'),
    # Vehicle overview page. Go to base url + overview/2016/honda/accord/
    url(r'^overview/(?P<year>[0-9]+)/(?P<make>[a-z]+[-.]?[a-z]+)/(?P<model>[0-9a-z]+[-.]?[0-9a-z]+)/$', views.overview, name='overview'),
]
