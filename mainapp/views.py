from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from mainapp.models import Class, Student, Remark, Lesson, Subject, HashCode, Grade
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

from mainapp.models import Teacher, Student, Parent, Absence
from mainapp.utils import isLogged, validateNewUserData, sendEMail


def home(request):
    # student = Student.objects.first()
    # print(student.getGradesWithSubjects)
    # print(student.getRemarks())
    # print(student.getAbsences())
    if isLogged(request):
        return HttpResponseRedirect("/redirect")
    return render(request, 'login.html')


def authenticate(request):  # todo url dla przekierowania i autoryzacji
    response = HttpResponseRedirect("/")
    response['wrongVals'] = 'true'
    if isLogged(request):
        response = HttpResponseRedirect("/redirect")

    elif 'username' in request.POST and 'password' in request.POST:
        try:
            user = User.objects.get(username=request.POST['username'])
        except:
            return response

        if check_password(request.POST['password'], user.password):
            request.session['username'] = request.POST['username']
            response = HttpResponseRedirect("/redirect")

    return response


def redirectLogged(request):
    user = User.objects.get(username=request.session['username'])
    response = HttpResponseRedirect("/")
    response['wrongVals'] = 'true'
    try:
        Teacher.objects.get(user=user)
        request.session["type"] = "teacher"
    except:
        pass
    try:
        Student.objects.get(user=user)
        request.session["type"] = "student"
    except:
        pass
    try:
        Parent.objects.get(user=user)
        request.session["type"] = "parent"
    except:
        pass

    response = HttpResponseRedirect("index")
    return response


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def addNewUser(request):
    registerErrors = validateNewUserData(request)
    if registerErrors.keys():
        response = HttpResponseRedirect('/register')
        for key in registerErrors.keys():
            response[key] = registerErrors[key]
        print(registerErrors)
        return response
    else:
        pass
        hashCode = HashCode.objects.get(code=request.POST['hashCode'])
        newUser = User()
        newUser.username = request.POST['username']
        newUser.email = request.POST['email']
        newUser.first_name = hashCode.name
        newUser.last_name = hashCode.surname
        newUser.password = make_password(request.POST['password'])
        newUser.save()
        if hashCode.teacher:
            hashCode.teacher.user = newUser
            hashCode.teacher.tempFullName = ''
            hashCode.teacher.save()
        if hashCode.student:
            hashCode.student.user = newUser
            hashCode.student.tempFullName = ''
            hashCode.student.save()
        if hashCode.parent:
            hashCode.parent.user = newUser
            hashCode.parent.tempFullName = ''
            hashCode.parent.save()
        hashCode.delete()

    return home(request)


def remark(request):
    if request.session["type"] == "teacher":
        return render(request, "teacherRemark.html")
    else:
        return render(request, "checkRemarks.html")


def fetchPeopleFromClass(request):
    selectedClass = request.POST["classSelected"]
    c = Class.objects.get(name=selectedClass)
    u = Student.objects.filter(clazz=c)
    l = []
    for item in u:
        l.append(str(item))

    return JsonResponse({'studentsList': l})


def saveRemark(request):
    remarkText = request.POST["remarkText"]
    # This is here for extending utility purposes
    clz = request.POST["clazz"]
    students = request.POST.getlist("students[]")
    tchr = request.session["username"]

    u = User.objects.get(username=tchr)
    t = Teacher.objects.get(user=u)
    sub = Subject.objects.get(name="Math")
    l = Lesson.objects.get(subject=sub)

    for s in students:
        u1 = User.objects.get(username=s)
        s = Student.objects.get(user=u1)
        Remark.objects.create(lesson=l, student=s, info=remarkText)

    return HttpResponse('')


def grade(request):
    if request.session["type"] == "teacher":
        return render(request, "teacherGrades.html")
    else:
        result = render(request, "checkGrades.html")
        return result


def saveGrade(request):
    forWhat = request.POST["forWhat"]
    # This is here for extending utility purposes
    students = request.POST.getlist("students[]")
    tchr = request.session["username"]
    grade = request.POST["grade"]

    u = User.objects.get(username=tchr)
    t = Teacher.objects.get(user=u)
    sub = Subject.objects.get(name="Math")
    l = Lesson.objects.get(subject=sub)

    for s in students:
        u1 = User.objects.get(username=s)
        s = Student.objects.get(user=u1)
        Grade.objects.create(grade=grade, lesson=l, student=s, forWhat=forWhat)

    return HttpResponse('')


def sendMail(request):
    return render(request, 'sendMail.html')


def sendMailServ(request):
    try:
        fromWhoUsername = request.session['username']
        toWhoUsername = request.POST['toWho']
        subject = request.POST['mailSubject']
        body = request.POST['mailBody']
    except:
        fromWhoUsername = ''
        toWhoUsername = ''
        subject = ''
        body = ''

    fromWho = None
    toWho = None

    if fromWhoUsername and toWhoUsername and subject and body:
        try:
            fromWho = User.objects.get(username=fromWhoUsername)
            toWho = User.objects.get(toWhoUsername)
            sendEMail(fromWho, toWho, subject, body)
        except:
            return HttpResponse(status=500)

    return HttpResponse('')


def settings(request):
    return render(request, 'settings.html')


def absences(request):
    if request.session["type"] == "teacher":
        return render(request, "teacherAbsences.html")
    else:
        return render(request, "checkAbsences.html")


def fetchClassSubject(request):
    teacher = request.session['username']
    clazz = request.POST['classSelected']

    u = User.objects.get(username=teacher)
    t = Teacher.objects.get(user=u)
    c = Class.objects.get(name=clazz)

    subjectList = []
    s = Subject.objects.filter(clazz=c, teacher=t)
    for item in s:
        subjectList.append(str(item))

    return JsonResponse({'subjectList': subjectList})


def fetchClassesLessons(request):
    subject = request.POST['subjectSelected']

    s = Subject.objects.get(name=subject)
    l = Lesson.objects.filter(subject=s)
    lessonList = []
    for item in l:
        lessonList.append(str(item))

    return JsonResponse({'lessonList': lessonList})


def fetchLessonAbsence(request):
    clazz = request.POST['classSelected']
    subj = request.POST['subjectSelected']
    date = request.POST['lessonDate']

    c = Class.objects.get(name=clazz)
    s = Subject.objects.get(name=subj, clazz=c)

    l = Lesson.objects.get(subject=s, date=date)
    students = c.getStudents()

    studentMap = {}
    for item in students:
        absence = None
        try:
            absence = Absence.objects.get(lesson=l, student=item)
        except:
            pass
        if absence is not None:
            studentMap[str(item)] = True
        else:
            studentMap[str(item)] = False

    return HttpResponse(json.dumps(studentMap))


def submitAbsences(request):
    clazz = request.POST['classSelected']
    subj = request.POST['subjectSelected']
    date = request.POST['lessonDate']
    abs = json.loads(request.POST["absMap"])


    c = Class.objects.get(name=clazz)
    s = Subject.objects.get(name=subj, clazz=c)
    l = Lesson.objects.get(subject=s, date=date)

    for a in abs:
        studUser = User.objects.get(username=a)
        stud = Student.objects.get(user=studUser)

        if abs[a] == 'true':


            try:
                Absence.objects.get(lesson=l, student=stud)
            except:
                absence = Absence()
                absence.lesson = l
                absence.student = stud
                absence.save()
        else:
            try:
                print("dupa")
                absence = Absence.objects.get(lesson=l, student=stud)
                print("dupa")
                absence.delete()
            except:
                continue


    return HttpResponse('')
