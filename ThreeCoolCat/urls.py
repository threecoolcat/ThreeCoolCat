"""ThreeCoolCat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from vali.views import ValiDashboardView

urlpatterns = [
    path('', RedirectView.as_view(url="/portal/index.html")),
    path('dashboard/', ValiDashboardView.as_view()),
    path(r'tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('shop/', include('shop.urls')),
    path('school/', include('school.urls')),
]

# 项目开发阶段可以用static管理上传文件或静态文件，以减少文件管理的工作量
# 项目在生产环境部署时， 上传文件或静态文件应该采用更可靠的方式管理， 比如采用nginx的静态资源管理
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# 文件上传目录
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 前端页面展现目录
urlpatterns += static(settings.PORTAL_URL, document_root=settings.PORTAL_ROOT)

if settings.DEBUG:
    # 开发阶段起用调试工具栏
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]