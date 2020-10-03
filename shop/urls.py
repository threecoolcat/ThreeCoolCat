from django.urls import path
from .views import BookView, VideoView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/books/', BookView.as_view()),
    path('api/videos/', VideoView.as_view()),
]

