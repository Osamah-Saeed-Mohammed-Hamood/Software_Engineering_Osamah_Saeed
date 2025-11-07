from django.contrib import admin

from .models import Student

# Register your models here.

admin.site.site_header = "U.S.I"
admin.site.index_title = "U.S.I"
admin.site.site_title = "U.S.I"

class StudentAdminForm(admin.ModelAdmin):
    list_display = ['f_name','l_name','gpa']
    list_display_links = ['l_name']
    list_editable = ['f_name']
    search_fields = ['f_name','l_name']
    list_filter = ['status','gpa']
    fields = ['f_name','l_name','gpa']
    list_per_page = 2


admin.site.register(Student,StudentAdminForm)