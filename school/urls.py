from django.conf.urls import url, include
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import SchoolView, CourseView, TeacherView

urlpatterns = [
    path('api/schools/', SchoolView.as_view()),
    url('^api/courses/$', CourseView.as_view()),
    url('^api/teachers/$', TeacherView.as_view()),
]

