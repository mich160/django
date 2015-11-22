from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
# Create your views here.
from django.template import RequestContext
from django.template.loader import get_template

from mainapp.models import Teacher, Student, Parent


def home(request):
    return render(request, 'home.html')


def authenticate(request):  # todo url dla przekierowania i autoryzacji
    response = HttpResponseRedirect("/")
    response['wrongVals'] = 'true'
    if 'username' in request.session:
        response = HttpResponseRedirect("/redirect")

    elif 'username' in request.POST and 'password' in request.POST:
        user = User.objects.get(username=request.POST['username'])
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
        response = HttpResponseRedirect("teachermain")
    except:
        pass
    try:
        Student.objects.get(user=user)
        response = HttpResponseRedirect('studentmain')
    except:
        pass
    try:
        Parent.objects.get(user=user)
        response = HttpResponseRedirect('parentmain')
    except:
        pass

    return response


def studentmain(request):
    return HttpResponse("placeholder")


def parentmain(request):
    return HttpResponse("placeholder")


def teachermain(request):
    return HttpResponse("placeholder")
