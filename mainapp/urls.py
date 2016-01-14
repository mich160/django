from django.conf.urls import include, url
from mainapp import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^authenticate', views.authenticate),
    url(r'^redirect', views.redirectLogged),
    url(r'^logout',views.logout),
    url(r'^index', views.index),
    url(r'^register', views.register),
    url(r'^addNewUser', views.addNewUser),
    url(r'^remark', views.remark),
    url(r'^fetchPeopleFromClass', views.fetchPeopleFromClass),
    url(r'^saveRemark', views.saveRemark),
    url(r'^grade', views.grade),
    url(r'^saveGrade', views.saveGrade),
    url(r'^sendMail', views.sendMail),
    url(r'^absences', views.absences),
    url(r'^fetchClassSubject', views.fetchClassSubject),
    url(r'^fetchClassesLessons', views.fetchClassesLessons),
    url(r'^fetchLessonAbsence', views.fetchLessonAbsence),
    url(r'^submitAbsences', views.submitAbsences),
    url(r'^mailServ', views.sendMailServ),
    url(r'^settings', views.settings),
    url(r'^changePassword', views.changePassword),
    url(r'^changeMail', views.changeMail),
    url(r'^timetable', views.timetable),
    url(r'^getTimeTablePDF', views.getTimeTablePDF)
]
