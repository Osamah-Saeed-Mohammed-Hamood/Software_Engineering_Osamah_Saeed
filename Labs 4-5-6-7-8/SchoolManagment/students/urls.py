from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("", views.home, name="home"),
    path('new/',views.newPage,name="newPage"),
    path('all/',views.read,name="all_students"),
    path('one/<int:id>/',views.read_one,name="student_one"),
    path('create/',views.create,name="Add_new_student"),
    path('update/<int:id>/',views.update,name="updateStudent"),
    path('delete/<int:id>/',views.delete,name="deleteStudent"),
]