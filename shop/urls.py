from django.conf.urls import url, include
from .views import BookView, VideoView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^api/books/$', BookView.as_view()),
    url('^api/videos/$', VideoView.as_view()),
]

