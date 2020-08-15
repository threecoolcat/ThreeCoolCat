from django.db import models
"""
网站通用的内容管理，内容的共性都是通过来列表来管理和展示， 
使用 abstract Model 的方式定义通用的字段，
每种内容有相同的字段和不同的字段， 将共同的字段定义在基础类中，
将不同的字段定义在本身的类中
并且不同的内容用不用的数据表保存
"""


# Create your models here.
class Article(models.Model):
    """文章"""
    id = models.AutoField(primary_key=True)
    title = models.CharField('标题', db_column='title', null=False, blank=False, default='', max_length=255)
    enabled = models.BooleanField('启用', db_column='enabled', null=False, blank=False, default=True)
    order_by = models.IntegerField('排序', db_column='order_by', null=True, blank=True, default=0)

    class Meta:
        abstract = True
        # db_table = 'article'
        # verbose_name = '文章'
        # verbose_name_plural = '文章管理'


class HotNews(Article):
    """热点新闻"""
    author = models.CharField('作者', db_column='author', null=True, blank=True, default='', max_length=255)
    link_url = models.CharField('原文链接', db_column='url', null=False, blank=False, default='', max_length=255)
    subtitle = models.CharField('副标题', db_column='subtitle', null=False, blank=False, default='', max_length=255)
    cover = models.ImageField('封面', db_column='cover', null=True, blank=True)
    content = models.TextField('内容', db_column='content')

    class Meta:
        managed = True
        db_table = 'hot_news'
        verbose_name = '热点新闻'
        verbose_name_plural = '热点新闻管理'


class TechnicalArticle(Article):
    author = models.CharField('作者', db_column='author', null=True, blank=True, default='', max_length=255)
    link_url = models.CharField('原文链接', db_column='url', null=False, blank=False, default='', max_length=255)
    subtitle = models.CharField('副标题', db_column='subtitle', null=False, blank=False, default='', max_length=255)
    cover = models.ImageField('封面', db_column='cover', null=True, blank=True)
    content = models.TextField('内容', db_column='content')

    class Meta:
        managed = True
        db_table = 'technical_article'
        verbose_name = '技术文章'
        verbose_name_plural = '技术文章管理'


class FriendLinks(Article):
    """友情链接"""
    url = models.CharField('链接', db_column='url', null=False, blank=False, default='', max_length=255)

    class Meta:
        managed = True
        db_table = 'friend_links'
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'
