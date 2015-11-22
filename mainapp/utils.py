def isLogged(request):
    if 'username' in request.session:
        return True
    else:
        return False