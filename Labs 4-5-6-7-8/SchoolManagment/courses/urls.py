from django.urls import path
from . import views

urlpatterns = [
    # مثال: صفحة البروفايل الرئيسية
    path('', views.home, name='home'),
]
