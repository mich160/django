from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$','mainapp.views.home'),
    url(r'^authenticate', 'mainapp.views.authenticate'),
    url(r'^redirect','mainapp.views.redirectLogged'),
    url(r'^student', 'mainapp.views.studentmain'),
    url(r'^teacher', 'mainapp.views.teachermain'),
    url(r'^parent', 'mainapp.views.parentmainmain')
]