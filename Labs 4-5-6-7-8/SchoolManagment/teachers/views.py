
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TeacherForm
from .models import Teacher
from django.contrib import messages

def teacher_list(request):
    storage = messages.get_messages(request)
    storage.used = True  

    teachers = Teacher.objects.all()
    teachers_count = Teacher.objects.all().count()
    return render(request, 'allTeachers.html', {'Teachers': teachers , "Teachers_count": teachers_count})

def read_one(request, id):
    teacher = Teacher.objects.get(id=id)
    return render(request, 'teacher_one.html', {'teacher': teacher})    

def add_teacher(request):
    if (request.method == 'POST'):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        department = request.POST.get('department')
        status = request.POST.get('status')
        new_teacher = Teacher(first_name = first_name,last_name = last_name , age = age , gender = gender , department = department , status = status )
        new_teacher.save()
        messages.success(request, "✅ تمت اضافة بيانات المعلم بنجاح")
        return redirect('teachers:teacher_list')  
    else:
        return render(request,'add_teacher.html')

def edit_teacher(request, id):
    if (request.method == 'POST'):
        teacher = Teacher.objects.get(id = id)
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.age = request.POST.get('age')
        teacher.gender = request.POST.get('gender')
        teacher.department = request.POST.get('department')
        teacher.status = request.POST.get('status')
        teacher.save()
        messages.success(request, "✅ تم تعديل بيانات المعلم بنجاح")
        return redirect('teachers:teacher_list')    
    else:
        teacher = Teacher.objects.get(id = id)
        return render(request,'edit_teacher.html',{"teacher":teacher})

def delete_teacher(request,id):
    Teacher.objects.get(id = id).delete()
    messages.success(request, "✅ تم حذف المعلم بنجاح")
    return redirect('teachers:teacher_list') 