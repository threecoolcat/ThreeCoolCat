from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from django.views.generic import TemplateView
from .serializer import HotNewsSerializer, TechnicalArticleSerializer, FriendLinksSerializer
from .models import HotNews, TechnicalArticle, FriendLinks
from school.models import Teacher, Course
from shop.models import Book, Video
# Create your views here.


class DashboardView(TemplateView):
    template_name = 'home/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # load sample data
        top_icons = [{"title": "教师", "value": Teacher.objects.count(), "style": "primary", "icon": "fa-users", "link": "/admin/school/teacher/"},
                     {"title": "课程", "value": Course.objects.count(), "style": "info", "icon": "fa-thumbs-o-up", "link": "/admin/school/course/"},
                     {"title": "图书", "value": Book.objects.count(), "style": "warning", "icon": "fa-files-o", "link": "/admin/shop/book/"},
                     {"title": "视频", "value": Video.objects.count(), "style": "danger", "icon": "fa-star", "link": "/admin/shop/video/"}]
        context['icons'] = top_icons
        return context


class HotNewsView(APIView):
    def get(self, request, *args, **kwargs):
        hotnews = HotNews.objects.all()
        pg = PageNumberPagination()
        items = pg.paginate_queryset(hotnews, request, self)
        serializer = HotNewsSerializer(items, many=True)
        return Response(serializer.data)


class TechArticleView(APIView):
    def get(self, request, *args, **kwargs):
        articles = TechnicalArticle.objects.all()
        pg = PageNumberPagination()
        items = pg.paginate_queryset(articles, request, self)
        serializer = TechnicalArticleSerializer(items, many=True)
        return Response(serializer.data)


class FriendLinksView(APIView):
    def get(self, request, *args, **kwargs):
        friends = FriendLinks.objects.filter(enabled=True).order_by('-order_by')[:4]
        pg = PageNumberPagination()
        items = pg.paginate_queryset(friends, request, self)
        serializer = FriendLinksSerializer(items, many=True)
        return Response(serializer.data)


# 自定义404页面
def page_not_found(request, exception=None, template_name='404.html'):
    context = {'hello': 'world'}
    return render(request, '404.html', context)

