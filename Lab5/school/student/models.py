from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=100, verbose_name="الاسم الأخير")
    age = models.IntegerField(verbose_name="العمر")
    stage = models.CharField(
        max_length=20,
        choices=[("first", "الأولى"), ("second", "الثانية"), ("third", "الثالثة")],
        verbose_name="المرحلة"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
