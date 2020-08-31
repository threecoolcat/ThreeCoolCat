from django.conf.urls import url, include
from .views import page_not_found, ArticlesView, TechArticleView, FriendLinksView, DashboardView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 传递命名参数，符合正则表达式.+的字符串，被命名为type，并传递给视图，视图中用kwargs接收
    url('^api/article/(?P<type>.+)/$', ArticlesView.as_view()),
    # url('^api/techarticle/$', TechArticleView.as_view()),
    url('^api/friends/$', FriendLinksView.as_view()),
]

