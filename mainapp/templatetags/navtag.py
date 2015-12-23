from django import template
from mainapp import utils
from mainapp.models import User, Teacher, Subject, Class, Student, Remark, Parent
from django.http import JsonResponse

register = template.Library()

@register.filter
def fetchClasses(request):
    u = User.objects.get(username=request.session["username"])
    t = Teacher.objects.get(user=u)
    s = Subject.objects.filter(teacher=t).distinct()
    for abc in s:
        print(abc)
        c = Class.objects.filter(subject=abc)
        print(c)
    tab = []
    for cls in c:
        tab.append(cls)
    print(tab)
    return tab


@register.filter
def fetchChilds(request):
    uname = request.session["username"]
    if utils.isStudent(uname):
        u = User.objects.get(username = uname)
        return [str(u.first_name) + " " + str(u.last_name)]
    else:
        u = User.objects.get(username = uname)
        p = Parent.objects.get(user = u)
    return p.fetchChild()


@register.filter
def fetchGrades(childName):
    childNameTable = childName.split(" ")
    child = User.objects.get(first_name=childNameTable[0], last_name=childNameTable[1])
    if utils.isStudent(child):
        u = User.objects.get(username = child)
        s = Student.objects.get(user=u)
        return s.getGradesWithSubjects


@register.filter
def fetchRemarks(uname):
    childNameTable = uname.split(" ")
    u = User.objects.get(first_name=childNameTable[0], last_name=childNameTable[1])
    s = Student.objects.get(user=u)
    r = Remark.objects.filter(student=s)
    remarkArr = []
    for remark in r:
        singleRemark = {}
        singleRemark['teacher']=str(remark.teacher.user.first_name + " " + remark.teacher.user.last_name)
        singleRemark['info'] = str(remark.info)
        remarkArr.append(singleRemark)
    return remarkArr


@register.filter
def fetchParents(request):
    user = User.objects.get(username=request.session["username"])
    currentTeacher = Teacher.objects.get(user=user)
    teacherClasses = currentTeacher.getClasses()
    students = []
    parents = set()
    for clazz in teacherClasses:
        clazzStudents = clazz.getStudents()
        for student in clazzStudents:
            students.append(student)
    for student in students:
        studentParents = student.parents.all()
        for parent in studentParents:
            parents.add(parent)
    return parents


@register.filter
def fetchAbsences(childName):
    childNameTable = childName.split(" ")
    child = User.objects.get(first_name=childNameTable[0], last_name=childNameTable[1])
    if utils.isStudent(child):
        u = User.objects.get(username = child)
        s = Student.objects.get(user=u)
        return s.getAbsences



