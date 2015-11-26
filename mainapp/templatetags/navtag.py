from django import template
from mainapp import utils
from mainapp.models import User, Teacher, Subject, Class, Student, Remark
from django.http import JsonResponse



register = template.Library()

@register.filter
def fetchClasses(request):
    u = User.objects.get(username = request.session["username"])
    t = Teacher.objects.get(user = u)
    s = Subject.objects.filter(teacher = t).values('clazz')
    c = Class.objects.get(subject = s)
    tab = []
    tab.append(c);
    return tab

@register.filter
def fetchChilds(request):
    uname = request.session["username"]
    if(utils.isStudent(uname)):
        return [uname]
    else:
        u = Users.objects.get(username = uname)
        p = Parent.objects.get(username = uname)
        s = Student.objects.filter(parents = p)
        
    return JsonResponse({ 'studentsList': s })
   
@register.filter 
def fetchRemarks(uname):
    u = User.objects.get(username = uname)
    s = Student.objects.get(user = u)
    r = Remark.objects.filter(student = s)
    remarkArr = []
    for remark in r:
        singleRemark = {}
        singleRemark['lesson'] = str(remark.lesson)
        singleRemark['info'] = str(remark.info.encode('utf-8'))
        remarkArr.append(singleRemark)
    
    
    
    return remarkArr
