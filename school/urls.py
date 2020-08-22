from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from .views import CourseView, TeacherView

urlpatterns = [
    url('^api/courses/$', CourseView.as_view()),
    url('^api/teachers/$', TeacherView.as_view()),
]

