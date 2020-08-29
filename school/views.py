from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import School, Course, Teacher
from django.views.decorators.csrf import csrf_exempt
from .serializer import CourseSerializer, SchoolSerializer, TeacherSerializer
# Create your views here.


# @csrf_exempt
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

    # @csrf_exempt
    def post(self, request):
        data = request.data
        course = Course.objects.get(id=data['id'])
        if course:
            course.status = data['status']
            course.save()
            return JsonResponse({"success": 1})
        else:
            return JsonResponse({"success": 0})


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
