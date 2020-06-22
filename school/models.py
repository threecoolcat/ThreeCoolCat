from django.db import models

# Create your models here.


class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('名称', db_column='name', null=True, blank=True, max_length=255)
    cover = models.CharField('封面图', db_column='cover', null=True, blank=True, max_length=255)
    # 简码用于页面识别,只有主站默认为空
    short_code = models.CharField('简码', db_column='short_code', null=True, blank=True, max_length=255, default='')
    intro = models.TextField('简介', db_column='intro', null=True, blank=True)
    address = models.CharField('地址', db_column='address', null=True, blank=True, max_length=255)
    linkman = models.CharField('联系人', db_column='linkman', null=True, blank=True, max_length=255)
    phone = models.CharField('联系电话', db_column='phone', null=True, blank=True, max_length=255)
    order_by = models.IntegerField('排序', db_column='order_by', null=True, blank=True, default=0)

    class Meta:
        managed = True
        db_table = 'school'
        verbose_name = '校区'
        verbose_name_plural = '校区管理'

    def __str__(self):
        return self.name
