from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here
class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course', null=True,blank=True)
    owner = models.ForeignKey(User, related_name='courses_created',null=True , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    code = models.CharField(max_length=10)
    desc = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name   = models.CharField(max_length=300)
    email  = models.EmailField(unique=True)
    phone  = models.CharField(max_length=12)
    date_joined = models.DateTimeField(auto_now_add=True)


    # def __str__(self):
    #     return self.name
    @property
    def course_title(self):
        return self.course.title               

class Module(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='module', null=True, blank=True)
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

# .title