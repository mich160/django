from django import template
from mainapp import utils
from mainapp.models import User, Teacher, Subject, Class, Student, Remark, Parent
from mainapp import subjectManager
from django.utils.html import format_html
from django.http import JsonResponse

register = template.Library()


@register.filter
def fetchClasses(request):
    u = User.objects.get(username=request.session["username"])
    t = Teacher.objects.get(user=u)
    s = Subject.objects.filter(teacher=t).distinct()
    for abc in s:
        c = Class.objects.filter(subject=abc)
    tab = []
    for cls in c:
        tab.append(cls)
    return tab


@register.filter
def fetchChilds(request):
    uname = request.session["username"]
    if utils.isStudent(uname):
        u = User.objects.get(username=uname)
        return [str(u.first_name) + " " + str(u.last_name)]
    else:
        u = User.objects.get(username=uname)
        p = Parent.objects.get(user=u)
    return p.fetchChild()


@register.filter
def fetchGrades(childName):
    childNameTable = childName.split(" ")
    child = User.objects.get(first_name=childNameTable[0], last_name=childNameTable[1])
    if utils.isStudent(child):
        u = User.objects.get(username=child)
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
        singleRemark['teacher'] = str(remark.teacher.user.first_name + " " + remark.teacher.user.last_name)
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
            if parent.user is not None:
                parents.add(parent)
    return parents


@register.filter
def fetchAbsences(childName):
    childNameTable = childName.split(" ")
    child = User.objects.get(first_name=childNameTable[0], last_name=childNameTable[1])
    if utils.isStudent(child):
        u = User.objects.get(username=child)
        s = Student.objects.get(user=u)
        return s.getAbsences


@register.filter
def fetchLessons(request):
    uname = request.session["username"]
    user = User.objects.get(username=uname)
    userRealName = user.first_name + " " + user.last_name
    timeTable = {}
    if utils.isTeacher(uname):
        timeTable[userRealName] = subjectManager.getTeacherTimeTable(userRealName)
        return timeTable
    elif utils.isStudent(uname):
        s = Student.objects.get(user=user)
        timeTable[userRealName] = subjectManager.getStudentTimeTable(s.clazz.name)
        return timeTable
    else:
        children = fetchChilds(request)
        for child in children:
            studentName = child.split(" ")
            studentFirstName = studentName[0]
            studentLastName = studentName[1]
            u = User.objects.get(first_name=studentFirstName, last_name=studentLastName)
            s = Student.objects.get(user=u)
            timeTable[child] = subjectManager.getStudentTimeTable(s.clazz.name)
        return timeTable


@register.filter
def generateTable(tableMap):
    lessonLookUp = {
        0: '8:00- 8:45',
        1: '9:00- 9:45',
        2: '10:00- 10:45',
        3: '11:00- 11:45',
        4: '12:00- 12:45',
        5: '13:00- 13:45',
        6: '14:00- 14:45',
        7: '15:00- 15:45',
    }
    daysInOrder = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    tableResult = "<table><thead><th class='lessonTimeHeader'>Dzwonki</th><th>Poniedziałek</th><th>Wtorek</th><th>Środa</th> <th>Czwartek</th><th>Piątek</th></thead><tbody>"

    for rowNumber in range(8):
        tableResult += "<tr><td class='lessonTime'>" + lessonLookUp[rowNumber] + "</td>"

        for day in daysInOrder:
            lesson = None
            for elem in tableMap[day]:
                if rowNumber + 1 == int(elem[1]):
                    lesson = "<td><span>" + elem[0] + "</span></td>"
            if lesson is not None:
                tableResult += lesson
            else:
                tableResult += "<td></td>"

        tableResult += "</tr>"

    tableResult += "</tbody></table>"
    return format_html(tableResult)
