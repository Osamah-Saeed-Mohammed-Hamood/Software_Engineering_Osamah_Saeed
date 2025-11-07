from django.db import models
from students.models import Student

class Teacher(models.Model):
    GENDER_CHOICES = [
        ('ذكر', 'ذكر'),
        ('أنثى', 'أنثى'),
    ]

    STATUS_CHOICES = [
        ('نعم', 'نعم'),
        ('لا', 'لا'),
    ]

    first_name = models.CharField(max_length=50, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=50, verbose_name="الاسم الأخير")
    age = models.PositiveIntegerField(verbose_name="العمر")
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES, verbose_name="الجنس")
    department = models.CharField(max_length=100, verbose_name="القسم")
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, verbose_name="منتظم")
    students = models.ManyToManyField(Student, related_name="teachers", verbose_name="الطلاب")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
