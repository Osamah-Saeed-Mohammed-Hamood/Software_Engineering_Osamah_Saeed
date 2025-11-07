from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, "list.html", {"students": students})

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")  # لازم تعرف URL بهذا الاسم
    else:
        form = StudentForm()
    return render(request, "add.html", {"form": form})
