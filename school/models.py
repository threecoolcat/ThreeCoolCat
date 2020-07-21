from django.db import models


# Create your models here.
class CourseInSchool(models.Model):
    id = models.AutoField(primary_key=True)
    school = models.ForeignKey('school.School', on_delete=models.CASCADE, verbose_name='校区', null=True, blank=True, related_name='schools', db_column='school_id')
    course = models.ForeignKey('school.Course', on_delete=models.CASCADE, verbose_name='课程', null=True, blank=True, related_name='courses', db_column='course_id')


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

    courses = models.ManyToManyField('Course', verbose_name='课程',
                                     through='CourseInSchool', through_fields=('school', 'course'))

    class Meta:
        managed = True
        db_table = 'school'
        verbose_name = '校区'
        verbose_name_plural = '校区管理'

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('名称', db_column='name', null=False, blank=False, default='', max_length=255)
    intro = models.TextField('简介', db_column='intro', null=True, blank=True)
    enabled = models.BooleanField('启用', db_column='enabled', null=False, blank=False, default=True)
    order_by = models.IntegerField('排序', db_column='order_by', null=True, blank=True, default=0)

    class Meta:
        managed = True
        db_table = 'course'
        verbose_name = '课程'
        verbose_name_plural = '课程管理'

    def __str__(self):
        return self.name
