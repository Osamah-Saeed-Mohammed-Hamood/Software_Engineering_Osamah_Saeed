from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="اسم المستخدم", widget=forms.TextInput(attrs={
        'placeholder': 'أدخل اسم المستخدم',
        'autocomplete': 'off',
    }))
    email = forms.EmailField(
        label="البريد الإلكتروني",
        required=True, # اجعله حقلاً مطلوباً
        widget=forms.EmailInput(attrs={
            'placeholder': 'أدخل بريدك الإلكتروني',
            'autocomplete': 'email'
        })
    )
    password1 = forms.CharField(label="كلمة المرور", widget=forms.PasswordInput(attrs={
        'placeholder': '••••••••'
    }))
    password2 = forms.CharField(label="تأكيد كلمة المرور", widget=forms.PasswordInput(attrs={
        'placeholder': '••••••••'
    }))

    class Meta:
        model = User
        fields = ['username', 'email']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="اسم المستخدم", widget=forms.TextInput(attrs={
        'placeholder': 'أدخل اسم المستخدم أو البريد الإلكتروني',
        'autocomplete': 'username',
    }))
    password = forms.CharField(label="كلمة المرور", widget=forms.PasswordInput(attrs={
        'placeholder': '••••••••',
        'autocomplete': 'current-password',
        'id': 'id_password' # Ensure the ID is predictable for JS
    }))

