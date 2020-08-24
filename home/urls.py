from django.conf.urls import url, include
from .views import page_not_found, HotNewsView, TechArticleView, FriendLinksView, DashboardView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^api/hotnews/$', HotNewsView.as_view()),
    url('^api/techarticle/$', TechArticleView.as_view()),
    url('^api/friends/$', FriendLinksView.as_view()),
]

