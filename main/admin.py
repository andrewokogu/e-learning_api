from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ['name', 'id', 'course','date_joined']

# admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ['title', 'code', 'desc', 'created']

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):

    list_display = ['course', 'title', 'description']


