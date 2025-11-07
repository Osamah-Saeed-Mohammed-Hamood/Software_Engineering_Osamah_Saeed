# admin.py

from django.contrib import admin
from django.contrib.auth.models import User
# 1. قم باستيراد UserAdmin الأصلي
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# 2. قم بإلغاء تسجيل النسخة الافتراضية
admin.site.unregister(User)

# 3. قم بإنشاء كلاس يرث من BaseUserAdmin (وليس ModelAdmin)
#    واستخدم ديكوريتور @admin.register لتسجيله
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    هنا يمكنك إضافة أو تعديل خصائص لوحة التحكم.
    """
    # مثال: إضافة حقل البريد الإلكتروني إلى قائمة العرض
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

    # مثال: إضافة فلترة حسب حالة الحساب (نشط/غير نشط)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    
    # يمكنك ترك الكلاس فارغًا إذا لم تكن لديك تخصيصات الآن
    # pass