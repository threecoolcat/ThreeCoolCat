from django.contrib import admin
from .models import Book, Video
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')