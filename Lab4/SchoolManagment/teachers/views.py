from django.shortcuts import render

from .data import context

# Create your views here.
def showTeachers(request):
    return render(request,'show.html',{"Teachers" : context})