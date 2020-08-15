from django.contrib import admin
from .models import Book, Video
from django.utils.safestring import mark_safe
# Register your models here.


# 定义管理类的基础类，将一些通用方法写进管理类 具体的管理类可以继承当前类并重新定义特有的方法
class BaseItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'cover_show', 'enabled', 'order_by')
    # 封面相关的定义是公用的， 子类无需重复写
    readonly_fields = ('cover_show', )

    def cover_show(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % obj.cover.url if obj.cover else '')
    # 自定义列的显示标题
    cover_show.short_description = '封面'


@admin.register(Book)
class BookAdmin(BaseItemAdmin):
    list_display = ('name', 'author', 'cover_show', 'sale_url', 'enabled', 'order_by')
    fieldsets = [
        ('基本信息', {'fields': ('name', 'author')}),
        ('封面', {'fields': ('cover', 'cover_show',)}),
        ('属性', {'fields': ('sale_url', 'unit_price', 'discount_price',)}),
        ('管理信息', {'fields': ('enabled', 'order_by')})
    ]


@admin.register(Video)
class VideoAdmin(BaseItemAdmin):
    list_display = ('name', 'author', 'cover_show', 'video_url', 'enabled', 'order_by')
    fieldsets = [
        ('基本信息', {'fields': ('name', 'author')}),
        ('封面', {'fields': ('cover', 'cover_show',)}),
        ('属性', {'fields': ('video_url',)}),
        ('管理信息', {'fields': ('enabled', 'order_by')})
    ]