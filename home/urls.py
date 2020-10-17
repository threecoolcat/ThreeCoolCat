from django.urls import path
from .views import ArticlesView, FriendLinksView, OperationLogView


urlpatterns = [
    # 传递命名参数type，类型为str，传递给视图，视图中用kwargs接收
    path('api/article/<str:type>/', ArticlesView.as_view()),
    # 不使用以下方法，改成使用上面一个方法，通过type区分
    # path('api/techarticle/', TechArticleView.as_view()),
    path('api/friends/', FriendLinksView.as_view()),
    path('api/log', OperationLogView.as_view()),
]

