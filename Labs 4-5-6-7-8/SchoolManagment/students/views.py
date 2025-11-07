from django.shortcuts import render , redirect
from .data import context
from django.contrib import messages

from .models import Student
from .Forms import StudentForm
from teachers.models import Teacher
from courses.models import Course
from profiles.models import Profile
from django.core.exceptions import ValidationError


# Create your views here.

def newPage(request):
    return render(request,'newWebPage.html',{"Students" : context})

def home(request):
    return render(request, "home.html")

def read(request):
    storage = messages.get_messages(request)
    storage.used = True  

    status = request.GET.get('q')
    if status == 'all' or status is None:
        Students = Student.objects.all().order_by('-gpa')
    else:
        Students = Student.objects.filter(status=status).order_by('-gpa')
    Students_count = Students.count()
    return render(request,'allStudents.html',{"Students" : Students, "Students_count": Students_count})

def read_one(request,id):
    student = Student.objects.get(id=id)
    return render(request,'student_one.html',{"student" : student})

def create(request):
    if (request.method == 'POST'):
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        age = request.POST.get('age')
        gpa = request.POST.get('gpa')
        level = request.POST.get('level')
        status = request.POST.get('status')
        report = request.POST.get('report')
        image = request.FILES.get('img')
        file_report = request.FILES.get('report_file')
        teacher_ids = request.POST.getlist('teachers')
        bio = request.POST.get('bio')
        course_ids = request.POST.getlist('courses')
        new_student = Student(f_name = f_name,l_name = l_name , age = age , gpa = gpa , level = level , status = status , report = report , image = image , file_report = file_report)
        
        try:
            new_student.full_clean()  # تحقق من صحة النموذج
            new_student.save()

            if bio:
                Profile.objects.create(student=new_student, user_type="student", bio=bio)
            
            if teacher_ids:
                new_student.teachers.set(teacher_ids)
                # ربط المقررات
            if course_ids:
                for cid in course_ids:
                    course = Course.objects.get(id=cid)
                    course.student = new_student
                    course.save()

            messages.success(request, "✅ تم إنشاء الطالب بنجاح")
            return redirect('students:all_students') 
        
        except ValidationError as e:
            for msg in e.messages:
                messages.error(request, msg)  
            teachers = Teacher.objects.all()
            all_courses = Course.objects.all()
            return render(request,'insert_student.html',
                        {"teachers": teachers ,
                        "all_courses": all_courses,
                        "old" : request.POST
                        }) 
    

    else:
        teachers = Teacher.objects.all()
        all_courses = Course.objects.all()
        return render(request, 'insert_student.html', {
            "teachers": teachers,
            "all_courses": all_courses
        })
    
def update(request,id):
    if (request.method == 'POST'):
        student = Student.objects.get(id = id)
        student.f_name = request.POST.get('f_name')
        student.l_name = request.POST.get('l_name')
        student.age = request.POST.get('age')
        student.gpa = request.POST.get('gpa')
        student.level = request.POST.get('level')
        student.status = request.POST.get('status')
        student.report = request.POST.get('report')
        # ✅ تحديث الصورة (اختياري)
        if 'img' in request.FILES:
            student.image = request.FILES['img']

        # ✅ تحديث ملف التقرير (اختياري)
        if 'report_file' in request.FILES:
            student.file_report = request.FILES['report_file']

        teacher_ids = request.POST.getlist('teachers')
        if teacher_ids:
            student.teachers.set(teacher_ids)
        else:
            student.teachers.clear()


        
        # ===== تحديث الملف الشخصي =====
        bio = request.POST.get('bio')
        profile, created = Profile.objects.get_or_create(
            student=student,
            defaults={'user_type': 'student'}
        )
        profile.bio = bio
        profile.save()

        # ===== تحديث المقررات الدراسية =====
        course_id = request.POST.get('course')

        if course_id:
            student.course = Course.objects.get(id=course_id)
        else:
            student.course = None
        student.save()


        messages.success(request, "✅ تم تعديل بيانات الطالب بنجاح")
        return redirect('students:all_students')  
        
    else:
        student = Student.objects.get(id = id)
        teachers = Teacher.objects.all()
        all_courses = Course.objects.all()
        student_course_id = student.course.id if student.course else None
        return render(request,'update_student.html',{"student":student,"teachers": teachers ,"all_courses": all_courses, "student_course_id": student_course_id})
    
def delete(request,id):
    Student.objects.get(id = id).delete()
    messages.success(request, "✅ تم حذف الطالب بنجاح")
    return redirect('students:all_students') 
