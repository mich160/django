from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=30)


class Student(models.Model):
    clazz = models.ForeignKey(Class)
    user = models.OneToOneField(User)


class Teacher(models.Model):
    user = models.OneToOneField(User)


class Parent(models.Model):
    user = models.OneToOneField(User)


class Subject(models.Model):
    name = models.CharField(max_length=60)
    clazz = models.ForeignKey(Class)
    teacher = models.ForeignKey(Teacher)


class Lesson(models.Model):
    subject = models.ForeignKey(Subject)
    clazz = models.ForeignKey(Class)
    date = models.DateTimeField()


class Grade(models.Model):
    grade = models.IntegerField()
    student = models.ForeignKey(Student)
    lesson = models.ForeignKey(Lesson)
    forWhat = models.CharField(max_length=100)


class Absence(models.Model):
    lesson = models.ForeignKey(Lesson)
    absenceStudent = models.ForeignKey(Student)


class Remark(models.Model):
    lesson = models.ForeignKey(Lesson)
    remarkStudent = models.ForeignKey(Student)
    info = models.CharField(max_length=200)
