from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'mainapp.views.home'),
    url(r'^authenticate', 'mainapp.views.authenticate'),
    url(r'^redirect', 'mainapp.views.redirectLogged'),
    url(r'^logout', 'mainapp.views.logout'),
    url(r'^index', 'mainapp.views.index'),
    url(r'^register', 'mainapp.views.register'),
    url(r'^addNewUser', 'mainapp.views.addNewUser'),
    url(r'^remark', 'mainapp.views.remark'),
    url(r'^fetchPeopleFromClass', 'mainapp.views.fetchPeopleFromClass'),
    url(r'^saveRemark', 'mainapp.views.saveRemark'),
    url(r'^grade', 'mainapp.views.grade'),
    url(r'^saveGrade', 'mainapp.views.saveGrade'),
    url(r'^sendMail', 'mainapp.views.sendMail'),
    url(r'^absences', 'mainapp.views.absences'),
    url(r'^fetchClassSubject', 'mainapp.views.fetchClassSubject'),
    url(r'^fetchClassesLessons', 'mainapp.views.fetchClassesLessons'),
    url(r'^fetchLessonAbsence', 'mainapp.views.fetchLessonAbsence'),
    url(r'^submitAbsences', 'mainapp.views.submitAbsences'),
    url(r'^mailServ', 'mainapp.views.sendMailServ'),
    url(r'^settings', 'mainapp.views.settings'),
    url(r'^changePassword', 'mainapp.views.settings'),
    url(r'^changeMail', 'mainapp.views.settings')
]
