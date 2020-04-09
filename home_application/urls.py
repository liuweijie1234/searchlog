# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.home),
    url(r'^index/$', views.home),
    url(r'^config/$', views.config),
)
