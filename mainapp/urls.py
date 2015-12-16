from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$','mainapp.views.home'),
    url(r'^authenticate', 'mainapp.views.authenticate'),
    url(r'^redirect','mainapp.views.redirectLogged'),
    url(r'^logout', 'mainapp.views.logout'),
    url(r'^index', 'mainapp.views.index'),
    url(r'^register', 'mainapp.views.register'),
    url(r'^addNewUser', 'mainapp.views.addNewUser'),
    url(r'^remark', 'mainapp.views.remark'),
    url(r'^fetchPeopleFromClass', 'mainapp.views.fetchPeopleFromClass'),
    url(r'^saveRemark', 'mainapp.views.saveRemark'),
    url(r'^grade', 'mainapp.views.grade'),
    url(r'^saveGrade', 'mainapp.views.saveGrade')
]