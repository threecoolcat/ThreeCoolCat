from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from home.utils import ThePager
# Create your views here.
from .serializer import BookSerializer, VideoSerializer
from .models import Book, Video


class BookView(APIView):
    def get(self, request, *args, **kwargs):
        if 'id' in request.query_params:
            book_id = request.query_params['id']
            books = Book.objects.filter(id=book_id)
        else:
            books = Book.objects.all()
        pg = ThePager()
        items = pg.paginate_queryset(books, request, self)
        serializer = BookSerializer(items, many=True)
        # return Response(serializer.data)
        return pg.get_paginated_response(serializer.data)


class VideoView(APIView):
    def get(self, request, *args, **kwargs):
        if 'id' in request.query_params:
            video_id = request.query_params['id']
            videos = Video.objects.filter(id=video_id)
        else:
            videos = Video.objects.all()
        pg = ThePager()
        items = pg.paginate_queryset(videos, request, self)
        serializer = VideoSerializer(items, many=True)
        return pg.get_paginated_response(serializer.data)
