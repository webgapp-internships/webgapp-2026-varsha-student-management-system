
from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'gender', 'department')

admin.site.register(Student, StudentAdmin)