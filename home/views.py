from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from django.views.generic import TemplateView
from .serializer import HotNewsSerializer, TechnicalArticleSerializer, FriendLinksSerializer
from .models import HotNews, TechnicalArticle, FriendLinks
# Create your views here.


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



class DashboardView(TechArticleView):
    template_name = 'home/dashboard.html'


# 自定义404页面
def page_not_found(request, exception=None, template_name='404.html'):
    context = {'hello': 'world'}
    return render(request, '404.html', context)

