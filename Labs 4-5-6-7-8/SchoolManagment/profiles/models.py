from django.db import models
from students.models import Student
from teachers.models import Teacher

class Profile(models.Model):
    user_type = models.CharField(max_length=10, choices=[("student", "Student"), ("teacher", "Teacher")])
    bio = models.TextField(verbose_name="السيرة الذاتية", null=True, blank=True)

    # OneToOne مع الطالب أو المعلم
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True, blank=True, related_name="profile")
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, null=True, blank=True, related_name="profile")

    def __str__(self):
        if self.student:
            return f"Profile of Student {self.student.f_name} {self.student.l_name}"
        elif self.teacher:
            return f"Profile of Teacher {self.teacher.first_name} {self.teacher.last_name}"
        return "Profile"
