from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم المقرر")
    description = models.TextField(verbose_name="وصف المقرر", null=True, blank=True)


    def __str__(self):
        return self.name

