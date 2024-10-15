from django.contrib import admin
from . import models
# Register your models here.

class Student(admin.ModelAdmin):
    list_display = ('Username', 'department', 'CurrentLevel')


admin.site.register(models.Student, Student)