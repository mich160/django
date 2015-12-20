from django.contrib.auth.models import User
from mainapp.models import Teacher, Student, HashCode
from django.core.mail import send_mail


def isLogged(request):
    if 'username' in request.session:
        return True
    else:
        return False


def validateNewUserData(request):
    errors = {}
    username = request.POST['username']
    email = request.POST['email']
    emailRepeated = request.POST['emailRep']
    hashcode = request.POST['hashCode']

    if not username:
        # mozna zastapic jakimis funkcjami walidacji pól np wykorzystujace regexy
        errors['username'] = 'Wrong username'
    if not email:
        errors['email'] = 'Wrong email'
    if email != emailRepeated:
        errors['emailRep'] = 'Emails don\'t match'
    if not hashcode:
        errors['hashcode'] = 'No hashcode'
    if not request.POST['password']:
        errors['password'] = 'Wrong password'
    if request.POST['password'] != request.POST['passwordRep']:
        errors['passwordRep'] = 'Passwords don\'t match'
    try:
        alreadyInDBUser = User.objects.get(username=username)
        errors['username'] = 'Username already exists'
    except:
        pass
    try:
        hashcodeInDB = HashCode.objects.get(code=hashcode)
    except:
        errors['hashcode'] = 'No hashcode set in database'

    return errors


def isStudent(user):
    try:
        u = User.objects.get(username=user)

        s = Student.objects.get(user=u)
        return True
    except:
        raise
        return False


def sendMail(fromWho, toWho, subject, body):
    send_mail(fromWho.first_name + " " + fromWho.last_name + ":" + subject, body,'placeholder@mail.com',[toWho.email], False, 'user', 'password');
