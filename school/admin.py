from django.contrib import admin
from .models import School, Course
# Register your models here.


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'linkman', 'phone')
    search_fields = ('name', 'address', 'linkman', 'phone')
    pass


@admin.register(Course)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro', 'enabled')
    pass
