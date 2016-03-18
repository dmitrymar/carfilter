from django.conf.urls import url
from . import views

carmake = "test"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.detail, name='detail'),

    url(r'^test/(?P<pk>\d+)/$', views.test, name='test'),

    # Vehicle overview page. Go to base url + overview/2016/honda/accord/coupe
    url(r'^(?i)overview/(?P<year>\d+)/(?P<make>[a-z]+[-.]?[a-z]+)/(?P<model>[\s\S]+)/(?P<body>[0-9a-z]+[-.]?[0-9a-z]+)/(?:(?P<version>[\s\S]*))?$', views.overview, name='overview'),
    # url(r'^(?i)overview/(?P<year>\d+)/(?P<make>[a-z]+[-.]?[a-z]+)/(?P<model>[0-9a-z-.]?[0-9a-z-]+)/(?P<body>[0-9a-z]+[-.]?[0-9a-z]+)/$', views.overview, name='overview'),
]
