from rest_framework import serializers
# from .models import *
from .models import Student, Course, Module

class StudentSerializer(serializers.ModelSerializer):

    course_title = serializers.ReadOnlyField()

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['id','course','course_title', 'name', 'email', 'phone']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        # fields = '__all__'
        fields = ['id','desc', 'code', 'title']


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id','course', 'title', 'description']
        # fields = '__all__'