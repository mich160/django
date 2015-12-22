from django.contrib.auth.models import User
from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=30)

    def getStudents(self):
        return Student.objects.filter(clazz=self)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    tempFullName = models.CharField(max_length=70, null=True, blank=True)
    user = models.OneToOneField(User, related_name='teacher', on_delete=models.CASCADE, null=True, blank=True)

    def getSubjects(self):
        return Subject.objects.filter(teacher=self)

    def getClasses(self):
        subjects = self.getSubjects()
        result = set()
        for subject in subjects:
            result.add(subject.clazz)
        return result

    def __str__(self):
        if not self.user:
            return str(self.tempFullName)
        else:
            return str(self.user)


class Parent(models.Model):
    tempFullName = models.CharField(max_length=70, null=True, blank=True)
    user = models.OneToOneField(User, related_name='parent', on_delete=models.CASCADE, null=True, blank=True)

    def fetchChild(self):
        children = Student.objects.filter(parents=self)
        studentList = []
        for item in children:
            studentList.append(item.user.username)
        return studentList

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

    @property
    def getGradesWithSubjects(self):
        # test: student = Student.objects.first()
        # print(student.getGradesWithSubjects())
        # print(student.getRemarks())
        # print(student.getAbsences())
        result = {}
        grades = Grade.objects.filter(student=self)

        subjects = Subject.objects.filter(clazz=self.clazz)
        for subject in subjects:
            result[subject] = [];
            lesson = Lesson.objects.filter(subject=subject)
            grades = Grade.objects.filter(lesson=lesson, student=self)
            for grade in grades:
                result[subject].append(grade)
        return result

    def getRemarks(self):
        return Remark.objects.filter(student=self)

    def getAbsences(self):
        return Absence.objects.filter(student=self)

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
        return str(self.name)


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
    modifier = models.CharField(max_length=1)

    def __str__(self):
        if str(self.modifier) is not '0':
            return str(self.modifier)+str(self.grade) + " " + str(self.lesson) + " " + str(self.student)
        else:
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
