from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$','mainapp.views.home'),
    url(r'^authenticate', 'mainapp.views.authenticate'),
    url(r'^redirect','mainapp.views.redirectLogged'),
    url(r'^finalizeLogin', 'mainapp.views.finalizeLogin'),
    url(r'^logout', 'mainapp.views.logout')
]