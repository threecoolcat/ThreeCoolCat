from django.conf.urls import url
from .views import IndexView, page_not_found, HotNewsView, TechArticleView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', IndexView.as_view()),
    url('^api/hotnews/$', HotNewsView.as_view()),
    url('^api/techarticle/$', TechArticleView.as_view()),
    url('^(index\\.html)?$', IndexView.as_view()),
    url('^404.html$', page_not_found),

]
# 项目开发阶段可以用static管理上传文件或静态文件，以减少文件管理的工作量
# 项目在生产环境部署时， 上传文件或静态文件应该采用更可靠的方式管理， 比如采用nginx的静态资源管理
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
