from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import School, Course, Teacher
from .serializer import CourseSerializer, SchoolSerializer, TeacherSerializer
# Create your views here.


class CourseView(APIView):
    def get(self, request, *args, **kwargs):
        if 'id' in request.query_params:
            courses = Course.objects.filter(id=request.query_params['id'])
        else:
            courses = Course.objects.all()
        pg = PageNumberPagination()
        items = pg.paginate_queryset(courses, request, self)
        serializer = CourseSerializer(items, many=True)
        return Response(serializer.data)


class TeacherView(APIView):
    def get(self, request, *args, **kwargs):
        if 'id' in request.query_params:
            teachers = Teacher.objects.filter(id=request.query_params['id'])
        else:
            teachers = Teacher.objects.all()
        pg = PageNumberPagination()
        items = pg.paginate_queryset(teachers, request, self)
        serializer = TeacherSerializer(items, many=True)
        return Response(serializer.data)
