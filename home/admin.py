from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

# 在第一个引用的APP中修改站点标题
# 修改站点的页面标题
admin.site.site_title = '三酷猫在线教育网'
# 修改站点的名称
admin.site.site_header = '三酷猫在线教育网'
# Register your models here.


# 同一个Admin类可以同时管理多个Model
# 项目前期，实体数据相似的实体类可以使用这种方式减少代码量
# 当Admin实体数据不满足要求时， 再单独定义Admin类
@admin.register(HotNews, TechnicalArticle)
class HotNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'cover_show', 'enabled', 'order_by')
    readonly_fields = ('cover_show',)

    def cover_show(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % obj.cover.url if obj.cover else '')

    cover_show.short_description = '封面'

    fieldsets = [
        ('基本信息', {'fields': ('title', 'subtitle', 'author', 'link_url')}),
        ('封面', {'fields': ('cover', 'cover_show',)}),
        ('内容', {'fields': ('content',)}),
        ('管理信息', {'fields': ('enabled', 'order_by')})
    ]


# @admin.register(TechnicalArticle)
# class TechnicalArticleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'link_url', 'cover_show', 'enabled', 'order_by')
#
#     def cover_show(self, obj):
#         return mark_safe(u'<img src="%s" width="100px" />' % obj.cover.url)
#     cover_show.short_description = '封面'
#
#     readonly_fields = ('cover_show',)
#     fieldsets = [
#         ('基本信息', {'fields': ('title', 'subtitle', 'author',  'link_url')}),
#         ('封面', {'fields': ('cover', 'cover_show',)}),
#         ('内容', {'fields': ('content',)}),
#         ('管理信息', {'fields': ('enabled', 'order_by')})
#     ]

@admin.register(FriendLinks)
class FriendLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'enabled', 'order_by')
    fieldsets = [
        ('基本信息', {'fields': ('title', 'url')}),
        ('管理信息', {'fields': ('enabled', 'order_by')})
    ]



