from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from django.views.generic import TemplateView
from .serializer import HotNewsSerializer, TechnicalArticleSerializer
from .models import HotNews, TechnicalArticle
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

# 自定义网站主页
class IndexView(TemplateView):
    template_name = 'home/index.html'

    # 页面加载时，给页面传值
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '三酷猫'
        return context


# 自定义404页面
def page_not_found(request, exception=None, template_name='404.html'):
    context = {'hello': 'world'}
    return render(request, '404.html', context)

