from django.contrib.auth.models import User
from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(User, related_name='teacher')

    def __str__(self):
        return str(self.user)


class Parent(models.Model):
    user = models.OneToOneField(User, related_name='parent')

    def __str__(self):
        return str(self.user)


class Student(models.Model):
    clazz = models.ForeignKey(Class)
    user = models.OneToOneField(User, related_name='student')
    parents = models.ManyToManyField(Parent, blank=True)

    def __str__(self):
        return str(self.user)


class Subject(models.Model):
    name = models.CharField(max_length=60)
    clazz = models.ForeignKey(Class)
    teacher = models.ForeignKey(Teacher)

    def __str__(self):
        return str(self.name) + str(self.clazz)


class Lesson(models.Model):
    subject = models.ForeignKey(Subject)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.subject) + " " + str(self.date)


class Grade(models.Model):
    grade = models.IntegerField()
    student = models.ForeignKey(Student)
    lesson = models.ForeignKey(Lesson)
    forWhat = models.CharField(max_length=100)

    def __str__(self):
        return str(self.grade) + " " + str(self.lesson) + " " + str(self.student)


class Absence(models.Model):
    lesson = models.ForeignKey(Lesson)
    student = models.ForeignKey(Student)

    def __str__(self):
        return str(self.lesson) + str(self.student)


class Remark(models.Model):
    lesson = models.ForeignKey(Lesson)
    student = models.ForeignKey(Student)
    info = models.CharField(max_length=200)

    def __str__(self):
        return str(self.student) + " " + str(self.lesson)


class HashCode(models.Model):
    code = models.CharField(max_length=30)
    userType = models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return str(self.code) + ": " + str(self.userType) + " " + str(self.name) + " " + str(self.surname)
