from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$','mainapp.views.home'),
    url(r'^authenticate', 'mainapp.views.authenticate'),
    url(r'^redirect','mainapp.views.redirectLogged'),
    url(r'^logout', 'mainapp.views.logout'),
    url(r'^index', 'mainapp.views.index'),
    url(r'^register', 'mainapp.views.register'),
    url(r'^addNewUser', 'mainapp.views.addNewUser')
    remark
    url(r'^remark', 'mainapp.views.remark')
]