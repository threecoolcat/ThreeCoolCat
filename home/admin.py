from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(HotNews)
class HotNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'enabled', 'order_by')


@admin.register(FriendLinks)
class FriendLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'enabled', 'order_by')


@admin.register(TechnicalArticle)
class TechnicalArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'link_url', 'enabled', 'order_by')

