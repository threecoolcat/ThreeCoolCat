from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
# Create your views here.
from .serializer import BookSerializer
from .models import Book


class BookView(APIView):
    def get(self, request, *args, **kwargs):

        #
        if 'id' in request.query_params:
            bookId = request.query_params['id']
            articles = Book.objects.filter(id=bookId)
        else:
            articles = Book.objects.all()
        pg = PageNumberPagination()
        items = pg.paginate_queryset(articles, request, self)
        serializer = BookSerializer(items, many=True)
        return Response(serializer.data)
