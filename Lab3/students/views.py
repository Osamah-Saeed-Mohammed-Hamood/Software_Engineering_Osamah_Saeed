from django.shortcuts import render

# Create your views here.
def index (request):
    name = {"fname" : "Osama Saeed"}
    return render(request,'index.html',name)

def home(request):
    return render(request,'home.html')

def list_students (request):
    students = {
        "name" : "Osama",
        "marks" : [100,99,98,97,96],
        "eachsub" : {"Software Engineering":100,
                    "Image Processing":96,
                    "Client and Server Programming":97}
    }
    return render(request,'showstudents.html',students)

def edit_students(request):
    students = {
        "total" : 286,
        "marks" : {"Software Engineering" : 100,
                "Image Processing" : 96,
                "Client and Server": 97}
    }
    return render(request,'editstudents.html',students)

def delete_students(request):
    return render(request,'deletestudents.html')