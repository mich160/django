from django.contrib.auth.models import User
from models import Teacher

def isLogged(request):
    if 'username' in request.session:
        return True
    else:
        return False

def isStudent(username):
    return True