from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render

# Create your views here.

from mainapp.models import Teacher, Student, Parent
from mainapp.utils import isLogged


def home(request):
    if isLogged(request):
        return HttpResponseRedirect("/redirect")
    return render(request, 'home.html')


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

    response = HttpResponseRedirect("finalizeLogin")
    return response


def logout(request):  # TODO usuwanie sesji
    request.session.flush()
    return HttpResponseRedirect('/')


def finalizeLogin(request):
    return render(request, 'genericNavbar.html')
