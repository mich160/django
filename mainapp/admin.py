from django.contrib import admin

# Register your models here.
from mainapp.models import *

admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Grade)
admin.site.register(Absence)
admin.site.register(Remark)
admin.site.register(HashCode)
