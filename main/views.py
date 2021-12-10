# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.serializers import serialiers
from .serializers import CourseSerializer, StudentSerializer, ModuleSerializer
# from rest_framework import serializers, status
from .serializers import *
from .models import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# from drf_yasg import openapi

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#             'rest_framework.authentication.TokenAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#             'rest_framework.permissions.IsAuthenticated',

#     ),}

@swagger_auto_schema(methods=['POST'], request_body=StudentSerializer())
# @permission_classes([IsAdminUser])
# @authentication_classes([BasicAuthentication])
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def students(request):
    if request.method == 'GET':
        student = Student.objects.all()
        # student = Student.objects.filter(user=request.user)
        serializer = StudentSerializer(student, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data) #get the posted data

        if serializer.is_valid(): #validate the data
            # serializer.save() #save the validated data
            if 'user' in serializer.validated_data.keys():
                serializer.validated_data.pop('user')
                
            object = Student.objects.create(**serializer.validated_data, user=request.user)
            serializer = StudentSerializer(object)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
            # return Response(serializer.data, status=status.HTTP_201_CREATED) #return response

        else: #if data is not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#This is to view the complete list of students hence i want only the admin to have access 
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        # student = Student.objects.filter(user=request.user)
        serializer = StudentSerializer(student, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)            

# A student can only view their record
User = get_user_model()
@api_view(['GET'])
# @permission_classes([IsAdminUser])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_s(request, student_id):
    
    if request.method == 'GET':
        # course = Course.objects.all()
        student = Student.objects.filter(user=request.user)
        serializer = StudentSerializer(student, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

#only the admin have the priviledge to PUT and DELETE
@swagger_auto_schema(methods=['PUT','DELETE'], request_body=StudentSerializer())
@api_view(['PUT', 'DELETE'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def get_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        data={
            'error':"Student not found"
            }
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    # if student.user != request.user:#new new
    #     raise PermissionDenied(detail='you do not have permission to perform this action')
    if request.method=='GET':
        serializer = StudentSerializer(student)
        data = {
                'status'  : True,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

        # return Response(serializer.data, status=status.HTTP_200_OK)
    #new testing code
    # elif request.method == 'POST':
    #     serializer = CourseSerializer(data = request.data) #get the posted data

    #     if serializer.is_valid(): #validate the data
    #         # serializer.save() #save the validated data
    #         if 'user' in serializer.validated_data.keys():#new
    #             serializer.validated_data.pop('user')
                
    #         object = Course.objects.create(**serializer.validated_data, user=request.user)
    #         serializer = CourseSerializer(object)#new
    #         return Response(serializer.data, status=status.HTTP_201_CREATED) #return response

    #     else: #if data is not valid
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()#new
            data = {
                'status'  : True,
                'message' : "Successful",
                'data' : serializer.data,#new
            }
            return Response(data, status=status.HTTP_201_CREATED)

            # return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            data = {#new
                'status'  : False,
                'message' : "Unsuccessful",
                'error' : serializer.errors,
            }#new
            return Response(data, status = status.HTTP_400_BAD_REQUEST)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()

        data = {#new
                'status'  : True,
                'message' : "Deleted Successfully"
            }#new
        return Response(status=status.HTTP_204_NO_CONTENT)


# @swagger_auto_schema(methods=['POST'], request_body=CourseSerializer())
# User = get_user_model()
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAdminUser])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@permission_classes([TokenAuthentication])
def courses(request):

    if request.method == 'GET':
        course = Course.objects.all()
        # course = Course.objects.filter(user=request.IsAdminUser)
        serializer = CourseSerializer(course, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # elif request.method == 'POST':
    #     serializer = CourseSerializer(data = request.data) #get the posted data

    #     if serializer.is_valid(): #validate the data
    #         # serializer.save() #save the validated data
    #         if 'user' in serializer.validated_data.keys():#new
    #             serializer.validated_data.pop('user')
                
    #         object = Course.objects.create(**serializer.validated_data, user=request.user)
    #         serializer = CourseSerializer(object)#new
    #         return Response(serializer.data, status=status.HTTP_201_CREATED) #return response

    #     else: #if data is not valid
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



User = get_user_model()
@swagger_auto_schema(methods=['PUT','DELETE'], request_body=CourseSerializer())
# @authentication_classes([BasicAuthentication])
# @permission_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def get_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Student.DoesNotExist:
        data={
            'error':"Course not found"
            }
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    # if course.user != request.user:
    #     raise PermissionDenied(detail='You do not have permission to perform this action')

    # if request.method=='GET':
    #     serializer = CourseSerializer(course)

    #     data = {
    #             'status'  : True,
    #             'message' : "Successful",
    #             'data' : serializer.data,
    #         }
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data, partial=True)

        if serializer.is_valid():
            #  if course.user != request.user:
            serializer.save()

            data = {
                'status'  : True,
                'message' : "Successful",
                'data' : serializer.data,
            }
            return Response(data, status = status.HTTP_201_CREATED)

            # return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            data = {
                'status'  : False,
                'message' : "Unsuccessful",
                'error' : serializer.errors,
            }
            return Response(data, status = status.HTTP_400_BAD_REQUEST)

            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

            course.delete()
            data = {
                    'status'  : True,
                    'message' : "Deleted Successfully"
                }
        # else:  
        #     raise PermissionDenied(detail='You do not have permission to perform this action')  
        # if course.user != request.user:
            # raise PermissionDenied(detail='You do not have permission to perform this action')
        
        # elif User == IsAdminUser:
        # else:    
        #     course.delete()

        #     data = {
        #             'status'  : True,
        #             'message' : "Deleted Successfully"
        #         }

            return Response(data, status = status.HTTP_204_NO_CONTENT)
    
        # return Response(status=status.HTTP_204_NO_CONTENT)

#create a course (only admin can create a course)
@swagger_auto_schema(methods=['POST'], request_body=CourseSerializer())
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @permission_classes([TokenAuthentication])
# @authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def create_course(request):
    

    if request.method == 'POST':
        serializer = CourseSerializer(data = request.data) #get the posted data

        if serializer.is_valid(): #validate the data
            # serializer.save() #save the validated data
            if 'user' in serializer.validated_data.keys():#new
                serializer.validated_data.pop('user')
                
            object = Course.objects.create(**serializer.validated_data, user=request.user)
            serializer = CourseSerializer(object)#new
            return Response(serializer.data, status=status.HTTP_201_CREATED) #return response

        else: #if data is not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#get course by  user id (course read)
User = get_user_model()
@api_view(['GET'])
# @permission_classes([IsAdminUser])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_course_by_id(request, course_id):
    
    if request.method == 'GET':
        # course = Course.objects.all()
        course = Course.objects.filter(user=request.user)
        serializer = CourseSerializer(course, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



# @swagger_auto_schema(methods=['POST'], request_body=ModuleSerializer())
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAdminUser])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@permission_classes([TokenAuthentication])
def modules(request):
    if request.method == 'GET':
        module = Module.objects.all()
        serializer = ModuleSerializer(module, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ModuleSerializer(data = request.data) #get the posted data

        if serializer.is_valid(): #validate the data
            serializer.save() #save the validated data
            return Response(serializer.data, status=status.HTTP_201_CREATED) #return response

        else: #if data is not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Only the admin can Edit and delete a course
@swagger_auto_schema(methods=['PUT','DELETE'], request_body=ModuleSerializer())
# # @authentication_classes([BasicAuthentication])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def get_module(request, module_id):
    try:
        module = Module.objects.get(id=module_id)
    except Module.DoesNotExist:
        data={
            'error':"Module not found"
            }
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    # if request.method=='GET':
    #     serializer = ModuleSerializer(module)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = ModuleSerializer(module, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # if module.user != request.user:
        #     raise PermissionDenied(detail='You do not have permission to perform this action')
        # else:    
        module.delete()
        data = {
                'status'  : True,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)
        # return Response(status=status.HTTP_204_NO_CONTENT)

#create a module (only admin can create a course)
@swagger_auto_schema(methods=['POST'], request_body=ModuleSerializer())
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @permission_classes([TokenAuthentication])
# @authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def create_module(request):
    

    if request.method == 'POST':
        serializer = ModuleSerializer(data = request.data) #get the posted data

        if serializer.is_valid(): #validate the data
            # serializer.save() #save the validated data
            if 'user' in serializer.validated_data.keys():#new
                serializer.validated_data.pop('user')
                
            object = Module.objects.create(**serializer.validated_data, user=request.user)
            serializer = ModuleSerializer(object)#new
            return Response(serializer.data, status=status.HTTP_201_CREATED) #return response

        else: #if data is not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


#get course by  user id (course read)
User = get_user_model()
@api_view(['GET'])
# @permission_classes([IsAdminUser])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_module_by_id(request, module_id):
    
    if request.method == 'GET':
        # course = Course.objects.all()
        module = Module.objects.filter(user=request.user)
        serializer = ModuleSerializer(module, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)                
