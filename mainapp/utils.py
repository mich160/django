from django.contrib.auth.models import User
from models import Teacher

def isLogged(request):
    if 'username' in request.session:
        return True
    else:
        return False
    
def isAdmin(request):
    # num_result=Admin.objects.filter(user = ).count()
    return False
    
def isTeacher(request):
    u = User.objects.get(username=request.session['username'])
    res = Teacher.objects.filter(user=u).count()
    return res
        
def isParent(request):
    return False
    
def isStudent(request):
    return False