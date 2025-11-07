# from django.urls import path
# from . import views

# app_name = 'teachers'

# # urlpatterns = [
# #     path('',views.showTeachers,name="showTeachers"),
# # ]



# urlpatterns = [
#     path('', views.teacher_list, name='teacher_list'),
#     path('add/', views.add_teacher, name='add_teacher'),
# ]

from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('one/<int:id>/',views.read_one,name="teacher_one"),
    path('add/', views.add_teacher, name='add_teacher'),
    path('edit/<int:id>/', views.edit_teacher, name='update_teacher'),
    path('delete/<int:id>/', views.delete_teacher, name='delete_teacher'),
]
