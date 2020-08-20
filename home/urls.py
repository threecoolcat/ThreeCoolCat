from django.conf.urls import url, include
from .views import IndexView, page_not_found, HotNewsView, TechArticleView, DashboardView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', IndexView.as_view()),
    url('^dashboard/$', DashboardView.as_view()),
    url('^api/hotnews/$', HotNewsView.as_view()),
    url('^api/techarticle/$', TechArticleView.as_view()),

]

