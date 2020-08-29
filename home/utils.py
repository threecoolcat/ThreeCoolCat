from rest_framework.pagination import PageNumberPagination


# 自定义分页器参数，
class ThePager(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'size'
