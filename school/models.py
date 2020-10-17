from django.db import models
from tinymce.models import HTMLField


class School(models.Model):
    """学校"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('名称', db_column='name', null=True, blank=True, max_length=255)
    cover = models.ImageField('封面', db_column='cover', upload_to='school', null=True, blank=True)
    # 简码用于页面识别,只有主站默认为空
    short_code = models.CharField('简码', db_column='short_code', null=True, blank=True, max_length=255, default='')
    intro = HTMLField('简介', db_column='intro', null=True, blank=True)
    address = models.CharField('地址', db_column='address', null=True, blank=True, max_length=255)
    linkman = models.CharField('联系人', db_column='linkman', null=True, blank=True, max_length=255)
    phone = models.CharField('联系电话', db_column='phone', null=True, blank=True, max_length=255)
    enabled = models.BooleanField('启用', db_column='enabled', null=False, blank=False, default=True)
    order_by = models.IntegerField('排序', db_column='order_by', null=True, blank=True, default=0)
    # courses = models.ManyToManyField('Course', verbose_name='课程',
    #                                  through='CourseInSchool', through_fields=('school', 'course'))

    class Meta:
        managed = True
        db_table = 'school'
        verbose_name = '校区'
        verbose_name_plural = '校区管理'

    def __str__(self):
        return self.name


# 教师、课程多对对关系表
class TeacherCourses(models.Model):
    teacher = models.ForeignKey(to='Teacher', on_delete=models.DO_NOTHING, to_field='id', db_column='teacher_id')
    course = models.ForeignKey(to='Course', on_delete=models.DO_NOTHING, to_field='id', db_column='course_id')

    class Meta:
        managed = False
        db_table = 'teacher_courses'


class Course(models.Model):
    """课程"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('名称', db_column='name', null=False, blank=False, default='', max_length=255)
    cover = models.ImageField('封面', db_column='cover', upload_to='course', null=True, blank=True)
    intro = HTMLField('简介', db_column='intro', null=True, blank=True)
    period = models.CharField('单课时长', db_column='period', null=True, blank=True, max_length=100)
    # period_amount = models.CharField('学期课时', db_column='period_amount', null=True, blank=True, max_length=100)
    start_date = models.DateField('开课日期', db_column='start_date', null=True, blank=True)
    category = models.IntegerField('类别', db_column='category', null=True, blank=True, default=1, choices=[(1, '线下课程'), (2, '线上课程')])
    status = models.BooleanField('状态', db_column='status', null=False, blank=False, default=True)
    enabled = models.BooleanField('启用', db_column='enabled', null=False, blank=False, default=True)
    order_by = models.IntegerField('排序', db_column='order_by', null=True, blank=True, default=0)
    school = models.ForeignKey(verbose_name='学校', to=School, on_delete=models.DO_NOTHING, to_field='id', null=True,
                               blank=True)

    # 建立多对多关系
    teachers = models.ManyToManyField(to='Teacher', through=TeacherCourses, )

    class Meta:
        managed = True
        db_table = 'course'
        verbose_name = '课程'
        verbose_name_plural = '课程设置'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """教师表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('姓名', db_column='name', null=False, blank=False, default='', max_length=255)
    title = models.CharField('学位', db_column='title', null=False, blank=False, default='', max_length=255)
    duty = models.CharField('职位', db_column='duty', null=False, blank=False, default='', max_length=255)
    photo = models.ImageField('照片', db_column='photo', upload_to='teacherphoto', null=False, blank=False, default='')
    keyword = models.CharField('关键词', db_column='keyword', null=True, blank=True, default='', max_length=255)
    intro = HTMLField('简介', db_column='intro', null=True, blank=True)
    school = models.ForeignKey(verbose_name='学校', to=School, on_delete=models.DO_NOTHING, to_field='id', null=True,
                               blank=True)
    enabled = models.BooleanField('启用', db_column='enabled', null=False, blank=False, default=True)
    order_by = models.IntegerField('排序', db_column='order_by', null=True, blank=True, default=0)
    courses = models.ManyToManyField('Course', verbose_name='课程')

    class Meta:
        managed = True
        db_table = 'teacher'
        verbose_name = '教师'
        verbose_name_plural = '教师管理'

    def __str__(self):
        return self.name


# 报名表单数据
class Enroll(models.Model):
    id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School, verbose_name='学校', on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.DO_NOTHING)
    name = models.CharField('姓名', max_length=64)
    phone = models.CharField('手机号', max_length=20)
    content = models.CharField('内容', max_length=500, blank=True, default=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'school_enroll'
        verbose_name = '报名咨询'
        verbose_name_plural = '报名咨询管理'
