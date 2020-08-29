from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from home.utils import ThePager
from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse
from django.views.generic import TemplateView

from .serializer import HotNewsSerializer, TechnicalArticleSerializer, FriendLinksSerializer, OperationLogSerializer
from .models import HotNews, TechnicalArticle, FriendLinks, OperationLog
from school.models import Teacher, Course
from shop.models import Book, Video
# Create your views here.


class DashboardView(TemplateView):
    template_name = 'home/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # load sample data
        top_icons = [{"title": "教师",
                      "value": Teacher.objects.count(),
                      "style": "primary",
                      "icon": "fa-users",
                      "link": "/admin/school/teacher/"},
                     {"title": "课程",
                      "value": Course.objects.count(),
                      "style": "info",
                      "icon": "fa-thumbs-o-up",
                      "link": "/admin/school/course/"},
                     {"title": "图书",
                      "value": Book.objects.count(),
                      "style": "warning",
                      "icon": "fa-files-o",
                      "link": "/admin/shop/book/"},
                     {"title": "视频",
                      "value": Video.objects.count(),
                      "style": "danger",
                      "icon": "fa-star",
                      "link": "/admin/shop/video/"}]
        # 将拼好的对象返回给页面， 页面模板可以通过 icons 访问该对象
        context['icons'] = top_icons
        # 页面模板中，该变量用来控制用户菜单，由admin管理的页面包含此变量
        context['has_permission'] = True
        return context


class HotNewsView(APIView):
    def get(self, request, *args, **kwargs):
        hotnews = HotNews.objects.all()
        pg = ThePager()
        items = pg.paginate_queryset(hotnews, request, self)
        serializer = HotNewsSerializer(items, many=True)
        return pg.get_paginated_response(serializer.data)


class TechArticleView(APIView):
    def get(self, request, *args, **kwargs):
        articles = TechnicalArticle.objects.all()
        pg = ThePager()
        items = pg.paginate_queryset(articles, request, self)
        serializer = TechnicalArticleSerializer(items, many=True)
        return pg.get_paginated_response(serializer.data)


class FriendLinksView(APIView):
    def get(self, request, *args, **kwargs):
        friends = FriendLinks.objects.filter(enabled=True).order_by('-order_by')[:4]
        pg = ThePager()
        items = pg.paginate_queryset(friends, request, self)
        serializer = FriendLinksSerializer(items, many=True)
        return pg.get_paginated_response(serializer.data)


# 自定义404页面, 函数式视图
def page_not_found(request, exception=None, template_name='404.html'):
    # 返回错误信息
    context = {'e': exception}
    return render(request, '404.html', context)


class OperationLogView(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = OperationLogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': 1})
        else:
            return JsonResponse({'success': 0})
