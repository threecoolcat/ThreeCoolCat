from django.contrib import admin
# from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .models import School, Course, Teacher
# Register your models here.


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'linkman', 'phone', 'cover_show', 'enabled', 'order_by')
    search_fields = ('name', 'address', 'linkman', 'phone')
    readonly_fields = ('cover_show',)

    def cover_show(self, obj):
        # 使用位置参数格式化字符串
        return format_html('<img src="{0}" width="100px" />', obj.cover.url if obj.cover else '')
    # 自定义列的显示标题
    cover_show.short_description = '封面'

    fieldsets = [
        ('基本信息', {'fields': ('name', 'short_code', 'address', 'linkman', 'phone',)}),
        ('封面', {'fields': ('cover', 'cover_show')}),
        ('简介', {'fields': ('intro', )}),
        ('管理信息', {'fields': ('enabled', 'order_by')})
    ]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    class Media:
        # 引用js文件
        js = ['school/course.js']
    list_display = ('name', 'category', 'start_date', 'period', 'cover_show', 'lbl_status', 'enabled', 'order_by', 'lbl_operation')
    readonly_fields = ('cover_show',)

    def cover_show(self, obj):
        return format_html('<img src="%s" width="100px" />' % obj.cover.url if obj.cover else '')
    # 自定义列的显示标题
    cover_show.short_description = '封面'

    def lbl_status(self, obj):
        return format_html('上架' if obj.status else '下架')

    lbl_status.short_description = '上架状态'

    def lbl_operation(self, obj):
        if obj.status:
            # 使用 命名参数格式化字符串
            return format_html('<a href="javascript:void(0)" onclick="update({id}, {status})">下架</a>', id=obj.id, status=0)
        else:
            return format_html('<a href="javascript:void(0)" onclick="update({id}, 1)">上架</a>', id=obj.id)

    lbl_operation.short_description = '操作'
    fieldsets = [
        ('基本信息', {'fields': ('name', 'category', 'start_date', 'period',)}),
        ('封面', {'fields': ('cover', 'cover_show')}),
        ('简介', {'fields': ('intro',)}),
        ('管理信息', {'fields': ('enabled', 'order_by')})
    ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'duty', 'photo_show', 'enabled', 'order_by')
    readonly_fields = ('photo_show',)
    filter_horizontal = ('courses', )

    def photo_show(self, obj):
        # 采用 % 格式化字符串
        return format_html('<img src="%s" width="100px" />' % obj.photo.url if obj.photo else '')

    # 自定义列的显示标题
    photo_show.short_description = '照片'
    fieldsets = [
        ('基本信息', {'fields': ('name', 'title', 'duty',)}),
        ('照片', {'fields': ('photo', 'photo_show')}),
        ('简介', {'fields': ('intro',)}),
        ('课程', {'fields': ('courses',)}),
        ('管理信息', {'fields': ('enabled', 'order_by')}),

    ]
