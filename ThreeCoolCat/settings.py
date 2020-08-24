"""
Django settings for ThreeCoolCat project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import pymysql
# 避免出现错误：
# django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.
pymysql.version_info = (1, 4, 6, 'final', 0)
# 启用pymysql的驱动模式， 否则不能用于django
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-gst4ca+$^^t7hasq3fpl(8w&t-w3rucbf&3-b=%%a@0$c4bqn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'vali',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'tinymce',
    'home.apps.HomeConfig',
    'school.apps.SchoolConfig',
    'shop.apps.ShopConfig',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 前端端分离时，要允许跨越请求
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8010',  # 本机调试地址
)
X_FRAME_OPTIONS = 'SAMEORIGIN'

if DEBUG:
    INSTALLED_APPS += ['debug_toolbar.apps.DebugToolbarConfig', ]
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_CONFIG = {
        # Toolbar options
        'JQUERY_URL': '/static/admin/js/vendor/jquery/jquery.min.js',
    }
# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
# ]
#
VALI_CONFIG = {
    'theme': 'blue',
    'dashboard': {'name': '管理中心', 'url': '/dashboard/'},
    'applist': {"order": "registry", "group": True},
    'font_awesome_url': 'font-awesome/4.7.0/css/font-awesome.min.css',
}
TINYMCE_DEFAULT_CONFIG = {'theme': 'silver', 'width': 600, 'height': 300, }

ROOT_URLCONF = 'ThreeCoolCat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 定义模版文件所在的路径
        'DIRS': ['templates'],
        # 是否读取应用下的模版
        # Django 加载模版的规则是： 最短路径原则， 也就是说
        # 如果出现多个同名的模版文件，
        # 1.在 django包的templstes目录下有 index.html
        # 2.在 当前项目的templates目录下有 index.html
        # 3.在 当前应用的templates目录下有 index.html
        # 当我们定义的视图 指向了index.html,会先找3 ，如果没找到会找2 ，还没找到会找1， 如果1也没有， 会抛出未找到文件的异常
        # 因此， 我们通过这个规则，可以对django自身的模版进行重新定义
        # 同理，我们要用到的静态资源文件（js文件，css文件，图片文件）也是相同的寻找原则

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ThreeCoolCat.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        # 引擎名称
        'ENGINE': 'django.db.backends.mysql',
        # 数据库名称
        'NAME': 'threecoolcat',
        # 用户名
        'USER': 'root',
        # 密码
        'PASSWORD': 'www.isoftstone.CoM',
        # 服务器地址
        'HOST': '127.0.0.1',
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# 静态资源的路径配置
STATIC_ROOT = os.path.join(BASE_DIR, 'static_dev')
STATIC_URL = '/static/'

# 网站前端资源目录
PORTAL_ROOT = os.path.join(BASE_DIR, 'portal')
PORTAL_URL = '/portal/'

# 文件上传的路径配置
MEDIA_URL = '/files/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'files').replace('\\', '/')

from django.contrib.admin.sites import AdminSite
# 修改站点的页面标题
AdminSite.site_title = '三酷猫课堂'
# 修改站点的名称
AdminSite.site_header = '三酷猫课堂'
# Register your models here.