from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.index,name='home'),
    path('read/<int:pk>/',views.read,name='read'),
    path('delete/<int:pk>/',views.delete,name='delete'),
]