from django.db import models
from courses.models import Course
from .validators import f_name_validetor,ext_validator,validate_image_mimetype

# Create your models here.

class Student(models.Model):
    Levels = (("1st","1st"),("2nd","2nd"),("3rd","3rd"),("4th","4th"))
    f_name = models.CharField(max_length=20,blank=False,null=False,validators=[f_name_validetor])
    l_name = models.CharField(max_length=20,null=False)
    age = models.PositiveIntegerField()
    level = models.CharField(choices=Levels,max_length=4)
    gpa = models.DecimalField(max_digits=5,decimal_places=2)
    status = models.BooleanField(default=True)
    report = models.TextField()
    image = models.ImageField(upload_to='images/%y/%m/',null=True,validators=[ext_validator,validate_image_mimetype])
    file_report = models.FileField(upload_to='files/%y/%m/',null=True)

    # الطالب يرتبط بمقرر واحد فقط
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        related_name="students",  # كل مقرر يمكن أن يرتبط بعدة طلاب
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.f_name} {self.l_name}"
    

