from django.shortcuts import render
from .data import context

# Create your views here.

def newPage(request):
    return render(request,'newWebPage.html',{"Students" : context})

def home(request):
    return render(request,'home.html')