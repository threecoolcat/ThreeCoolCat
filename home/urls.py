from django.conf.urls import url
from .views import IndexView, page_not_found

urlpatterns = [
    url('', IndexView.as_view()),
    url('^(index\\.html)?$', IndexView.as_view()),
    url('^404.html$', page_not_found),

]
