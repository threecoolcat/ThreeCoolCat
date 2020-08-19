from django.conf.urls import url
from .views import ValiDashboardView
urlpatterns = [
    url('^dashboard/', ValiDashboardView.as_view())
]