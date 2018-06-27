from django.conf.urls import url, include
from django.urls import path

from dj_parser import views

urlpatterns = [
    url(r'^tags/$', views.tag_list),
    url(r'^tags/(?P<pk>[0-9]+)$', views.tag_detail),
]