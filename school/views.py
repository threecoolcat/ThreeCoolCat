from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import School, Course, Teacher
from .serializer import CourseSerializer, SchoolSerializer, TeacherSerializer, EnrollSerializer
from home.utils import ThePager
# Create your views here.


# 学校
class SchoolView(APIView):
    def get(self, request, *args, **kwargs):
        if 'id' in request.query_params:
            schools = School.objects.filter(id=request.query_params['id'])
        else:
            schools = School.objects.all()
        pg = ThePager()
        items = pg.paginate_queryset(schools, request, self)
        serializer = SchoolSerializer(items, many=True)
        return pg.get_paginated_response(serializer.data)


# 课程
class CourseView(APIView):
    def get(self, request, *args, **kwargs):
        # 如果参数中有id，则返回一条记录
        # 否则返回全部记录
        if 'id' in request.query_params:
            courses = Course.objects.filter(id=request.query_params['id'])
        else:
            courses = Course.objects.all()
        if 'school' in request.query_params:
            courses = courses.filter(school__exact=request.query_params['school'])
        # 分页功能
        pg = ThePager()
        items = pg.paginate_queryset(courses, request, self)
        serializer = CourseSerializer(items, many=True)
        return pg.get_paginated_response(serializer.data)

    def post(self, request):
        print(request.user.username, ' is logined: ', request.user.is_authenticated)
        # 判断用户是否登录,仅登录用户允许提交
        if request.user.is_authenticated:
            data = request.data
            course = Course.objects.get(id=data['id'])
            if course:
                course.status = data['status']
                course.save()
                return JsonResponse({"success": 1})
        else:
            return JsonResponse({"success": 0})


# 教师
class TeacherView(APIView):
    def get(self, request, *args, **kwargs):
        if 'id' in request.query_params:
            teachers = Teacher.objects.filter(id=request.query_params['id'])
        else:
            teachers = Teacher.objects.all()
        if 'school' in request.query_params:
            courses = teachers.filter(school__exact=request.query_params['school'])
        pg = ThePager()
        items = pg.paginate_queryset(teachers, request, self)
        serializer = TeacherSerializer(items, many=True)
        return pg.get_paginated_response(serializer.data)


class EnrollView(APIView):
    def post(self, request):
        enroll = EnrollSerializer(data=request.data)
        if enroll.is_valid():
            enroll.save()
            return JsonResponse({'success': 1})
        else:
            return JsonResponse({'success': 0})
