from django.urls import path
from .views import SchoolView, CourseView, TeacherView

urlpatterns = [
    path('api/schools/', SchoolView.as_view()),
    path('api/courses/', CourseView.as_view()),
    path('api/teachers/', TeacherView.as_view()),
]

