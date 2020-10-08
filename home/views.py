from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from home.utils import ThePager
from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .serializer import HotNewsSerializer, ActiveNewsSerializer, TechnicalArticleSerializer, FriendLinksSerializer, OperationLogSerializer
from .models import HotNews, ActiveNews, TechnicalArticle, FriendLinks, OperationLog
from school.models import Teacher, Course
from shop.models import Book, Video
from django.db.models import Count
from datetime import datetime, date, timedelta
# Create your views here.
from django.db import connection

# 主页视图，计算基础统计信息
class DashboardView(TemplateView):
    template_name = 'home/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # load sample data
        top_icons = [{"title": "教师",
                      "value": Teacher.objects.filter(enabled=True).count(),
                      "style": "primary",
                      "icon": "fa-users",
                      "link": "/admin/school/teacher/"},
                     {"title": "课程",
                      "value": Course.objects.filter(enabled=True, status=True).count(),
                      "style": "info",
                      "icon": "fa-thumbs-o-up",
                      "link": "/admin/school/course/"},
                     {"title": "图书",
                      "value": Book.objects.filter(enabled=True).count(),
                      "style": "warning",
                      "icon": "fa-files-o",
                      "link": "/admin/shop/book/"},
                     {"title": "视频",
                      "value": Video.objects.filter(enabled=True).count(),
                      "style": "danger",
                      "icon": "fa-star",
                      "link": "/admin/shop/video/"}]
        # 将拼好的对象返回给页面， 页面模板可以通过 icons 访问该对象
        context['icons'] = top_icons
        # 近5天的日期
        dates = []
        data1 = []
        # for i in range(5):
        #     yesterday = (date.today() + timedelta(days=-i)).strftime("%Y-%m-%d")
        #     dates.insert(0, yesterday)
        # begin = date.today() + timedelta(days=-5)
        # end = date.today()
        # ol = OperationLog.objects.filter(create_time__range=[begin, end])
        with connection.cursor() as cursor:
            cursor.execute("""select  date_format(create_time, '%Y-%m-%d') date, count(id) cnt from operation_log group by date_format(create_time, '%Y-%m-%d')""")
            results = cursor.fetchall()

        for r in results:
            dates.append(r[0])
            data1.append(r[1])

        charts = [{
            "name": "linechart1", "title": "模块点击次数", "type": "Line",
            "labels": dates,
            "datasets": [
                {
                    "label": "dataset 1",
                    "fillColor": "rgba(220,220,220,0.2)",
                    "strokeColor": "rgba(220,220,220,1)",
                    "pointColor": "rgba(220,220,220,1)",
                    "pointStrokeColor": "#fff",
                    "pointHighlightFill": "#fff",
                    "pointHighlightStroke": "rgba(220,220,220,1)",
                    "data": data1
                }
            ]
        }, {
            "name": "piechart1", "title": "网站内容分布", "type": "Pie",
            "datasets": [
                {"value": Course.objects.filter(enabled=True, status=True).count(), "color": "#46BFBD", "highlight": "#5AD3D1", "label": "课程"},
                {"value": Book.objects.filter(enabled=True).count(), "color": "#77464A", "highlight": "#7F5A5E", "label": "图书"},
                {"value": Video.objects.filter(enabled=True).count(), "color": "#F7464A", "highlight": "#FF5A5E", "label": "视频"},
                {"value": Teacher.objects.filter(enabled=True).count(), "color": "#5A5F5E", "highlight": "#5A5F5E", "label": "教师"},
            ]
        }]
        context['charts'] = charts
        # 页面模板中，该变量用来控制用户菜单，由admin管理的页面包含此变量
        context['has_permission'] = True
        return context


# 根据文章类型， 返回不同的数据
class ArticlesView(APIView):
    def get(self, request, *args, **kwargs):
        pg = ThePager()
        if kwargs['type'] and kwargs['type'] == 'news':
            articles = HotNews.objects.all()

            items = pg.paginate_queryset(articles, request, self)
            serializer = HotNewsSerializer(items, many=True)
        elif kwargs['type'] and kwargs['type'] == 'active':
            articles = ActiveNews.objects.all()
            items = pg.paginate_queryset(articles, request, self)
            serializer = ActiveNewsSerializer(items, many=True)
        elif kwargs['type'] and kwargs['type'] == 'tech':
            articles = TechnicalArticle.objects.all()
            items = pg.paginate_queryset(articles, request, self)
            serializer = TechnicalArticleSerializer(items, many=True)
        else:
            return JsonResponse({'success': 0, 'msg': 'wrong type', 'results': []})
        if 'id' in request.query_params:
            articles = articles.filter(id=request.query_params['id'])
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
        data = request.data
        data['user_agent'] = request.stream.META['HTTP_USER_AGENT']
        serializer = OperationLogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': 1})
        else:
            return JsonResponse({'success': 0})

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(OperationLogView, self).dispatch(request, *args, **kwargs)