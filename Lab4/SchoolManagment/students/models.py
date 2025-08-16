from django.db import models

# Create your models here.

class Student(models.Model):
    Levels = (("1st","1st"),("2nd","2nd"),("3rd","3rd"),("4th","4th"))
    f_name = models.CharField(max_length=20,default="User")
    l_name = models.CharField(max_length=20,default="User",null=False)
    age = models.IntegerField()
    level = models.CharField(choices=Levels,max_length=4)
    gpa = models.DecimalField(max_digits=5,decimal_places=2)
    status = models.BooleanField(default=True)
    report = models.TextField()
    def __str__(self):
        return f"{self.f_name} {self.l_name}"