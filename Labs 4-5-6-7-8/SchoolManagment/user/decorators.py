
from django.http import HttpResponse as httpResponse 
from django.shortcuts import redirect   

def isadmin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.exists:
            group = request.user.groups.all()[0].name
            print(group)
            if group == 'admin':
                return view_func(request, *args, **kwargs)
            else:
                return httpResponse("401 - Unauthorized")
        else:
            return httpResponse("401 - Unauthorized")
    return wrapper_func

def isloggedin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('students:home')    
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func