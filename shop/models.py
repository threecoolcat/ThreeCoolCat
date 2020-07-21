from django.db import models


# Create your models here.
class Item:
    """物品基础类"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('名称', db_column='name', null=False, blank=False, default='', max_length=255)
    unit_price = models.DecimalField('单价', db_column='unit_price', null=True, blank=False)
    discount_price = models.DecimalField('折扣价', db_column='discount_price', null=True, blank=False)

    class Meta:
        # 抽象类， 不生成实体表
        abstract = True


class Book(Item):
    """图书"""
    author = models.CharField('作者', db_column='author', max_length=100, null=True, blank=True)
    sale_url = models.CharField('购买链接', db_column='sale_url', max_length=100, null=True, blank=True)

    class Meta:
        managed = True


class Video(Item):
    """教学视频"""
    video_url = models.CharField('视频地址', db_column='video_url', max_length=100, null=True, blank=True)

    class Meta:
        managed = True

