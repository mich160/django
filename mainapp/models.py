from django.contrib.auth.models import User
from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    tempFullName = models.CharField(max_length=70, null=True, blank=True)
    user = models.OneToOneField(User, related_name='teacher', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if not self.user:
            return str(self.tempFullName)
        else:
            return str(self.user)


class Parent(models.Model):
    tempFullName = models.CharField(max_length=70, null=True, blank=True)
    user = models.OneToOneField(User, related_name='parent', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if not self.user:
            return str(self.tempFullName)
        else:
            return str(self.user)


class Student(models.Model):
    tempFullName = models.CharField(max_length=70, null=True, blank=True)
    clazz = models.ForeignKey(Class)
    user = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE, null=True, blank=True)
    parents = models.ManyToManyField(Parent, blank=True)

    def getGrades(self):
        result = {}
        grades = Grade.objects.filter(student = self)
        for grade in grades:
            lesson = Lesson.objects.filter(grade=grade).first()
            subject = lesson.subject
            try:
                if result[subject]:
                    pass
            except:
                result[subject] = []
            result[subject].append(grade)
        return result


    def __str__(self):
        if not self.user:
            return str(self.tempFullName)
        else:
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
    teacher = models.OneToOneField(Teacher, blank=True, null=True)
    student = models.OneToOneField(Student, blank=True, null=True)
    parent = models.OneToOneField(Parent, blank=True, null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    studentClazz = models.ForeignKey(Class, blank=True, null=True)

    def __str__(self):
        return str(self.code) + ": " + " " + str(self.name) + " " + str(self.surname)
