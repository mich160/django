from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from mainapp.models import Class, Student, Remark, Lesson, Subject
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.http import JsonResponse


# Create your views here.

from mainapp.models import Teacher, Student, Parent
from mainapp.utils import isLogged


def home(request):
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


def logout(request):  # TODO usuwanie sesji
    request.session.flush()
    return HttpResponseRedirect('/')


def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def addNewUser(request):
    
    # Some registration logic here
    
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
        
    # tutaj powinno wysylac username(do option value) + imie i nazwisko(do wyswietlenia) 
    
    return JsonResponse({ 'studentsList': l })

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
        
    
    
    
    
    
    
    
    
    
    
    
    
