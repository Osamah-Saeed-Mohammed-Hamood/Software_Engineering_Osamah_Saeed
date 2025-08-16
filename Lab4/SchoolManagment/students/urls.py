from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('new/',views.newPage,name="newPage"),
    # path('page/',views.page,name="page"),
    # path('all/',views.read,name="students"),
    # path('one/',views.read_one,name="student_one"),
    # path('create/',views.create,name="newStudent"),
    # path('update/',views.update,name="updateStudent"),
    # path('delete/',views.delete,name="deleteStudent"),
]