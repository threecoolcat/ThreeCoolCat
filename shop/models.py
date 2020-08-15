from django.db import models
"""商店的内容定义，采用 abstract 方式"""


# Create your models here.
class Item(models.Model):
    """物品基础类"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('名称', db_column='name', null=False, blank=False, default='', max_length=255)
    unit_price = models.DecimalField('单价', db_column='unit_price', null=True, blank=False,
                                     decimal_places=2, max_digits=8)
    discount_price = models.DecimalField('折扣价', db_column='discount_price', null=True, blank=False,
                                         decimal_places=2, max_digits=8)

    class Meta:
        # 抽象类， 不生成实体表
        abstract = True


class Book(Item):
    author = models.CharField('作者', db_column='author', max_length=100, null=True, blank=True)
    sale_url = models.CharField('购买链接', db_column='sale_url', max_length=100, null=True, blank=True)

    class Meta:
        managed = True
        abstract = False
        db_table = 'book'
        verbose_name = '图书'
        verbose_name_plural = '图书管理'

    def __str__(self):
        return self.name


class Video(Item):
    """教学视频"""
    author = models.CharField('作者', db_column='author', max_length=100, null=True, blank=True)
    video_url = models.CharField('视频地址', db_column='video_url', max_length=100, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'video'
        verbose_name = '视频'
        verbose_name_plural = '视频管理'

    def __str__(self):
        return self.name
