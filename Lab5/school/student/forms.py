from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'stage']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل الاسم الأول'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل الاسم الأخير'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل العمر'}),
            'stage': forms.Select(attrs={'class': 'form-select'}),
        }
