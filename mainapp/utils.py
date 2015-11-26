from django.contrib.auth.models import User
from models import Teacher, Student

def isLogged(request):
    if 'username' in request.session:
        return True
    else:
        return False

def isStudent(username):
    try:
        u = User.objects.get(username)
        s = Student.objects.get(user = u)
        return True
    except:
        return False
    
