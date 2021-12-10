from django.urls import path
from .views import *

urlpatterns = [
    path('students/', students),
    
    path('students/<int:student_id>/', get_s),
    path('student/', get_student_list),
    path('student/<int:student_id>/', get_student),
    path('courses/', courses),
    path('course/', create_course),
    path('courses/<int:course_id>/', get_course_by_id),
    path('course/<int:course_id>/', get_course),
    path('modules/', modules),
    path('module/', create_module),
    path('modules/<int:module_id>/', get_module_by_id),
    path('module/<int:module_id>/', get_module),
]