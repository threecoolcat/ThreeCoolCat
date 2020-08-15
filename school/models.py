from django.db import models


# Create your models here.
class CourseInSchool(models.Model):
    """学校和课程的对应关系"""
    id = models.AutoField(primary_key=True)
    school = models.ForeignKey('school.School', on_delete=models.CASCADE, verbose_name='校区', null=True, blank=True,
                               related_name='course_schools', db_column='school_id')
    course = models.ForeignKey('school.Course', on_delete=models.CASCADE, verbose_name='课程', null=True, blank=True,
                               related_name='school_courses', db_column='course_id')


class School(models.Model):
    """学校"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('名称', db_column='name', null=True, blank=True, max_length=255)
    cover = models.ImageField('封面', db_column='cover', upload_to='school', null=True, blank=True)
    # 简码用于页面识别,只有主站默认为空
    short_code = models.CharField('简码', db_column='short_code', null=True, blank=True, max_length=255, default='')
    intro = models.TextField('简介', db_column='intro', null=True, blank=True)
    address = models.CharField('地址', db_column='address', null=True, blank=True, max_length=255)
    linkman = models.CharField('联系人', db_column='linkman', null=True, blank=True, max_length=255)
    phone = models.CharField('联系电话', db_column='phone', null=True, blank=True, max_length=255)
    enabled = models.BooleanField('启用', db_column='enabled', null=False, blank=False, default=True)
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
    """课程"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('名称', db_column='name', null=False, blank=False, default='', max_length=255)
    cover = models.ImageField('封面', db_column='cover', upload_to='course', null=True, blank=True)
    intro = models.TextField('简介', db_column='intro', null=True, blank=True)
    period = models.CharField('课程时长', db_column='period', null=True, blank=True, max_length=100)
    period_amount = models.CharField('课时数量', db_column='period_amount', null=True, blank=True, max_length=100)
    category = models.IntegerField('类别', db_column='category', null=True, blank=True, default=1, choices=[(1, '线下课程'), (2, '线上课程')])
    enabled = models.BooleanField('启用', db_column='enabled', null=False, blank=False, default=True)
    order_by = models.IntegerField('排序', db_column='order_by', null=True, blank=True, default=0)

    class Meta:
        managed = True
        db_table = 'course'
        verbose_name = '课程'
        verbose_name_plural = '课程管理'

    def __str__(self):
        return self.name


class TeacherWithCourse(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey('school.Course', on_delete=models.CASCADE, verbose_name='课程', null=True, blank=True,
                               related_name='teacher_courses', db_column='course_id')
    teacher = models.ForeignKey('school.Teacher', on_delete=models.CASCADE, verbose_name='教师', null=True, blank=True,
                                related_name='course_teachers', db_column='teacher_id')

    class Meta:
        db_table = 'teacher_course'


class Teacher(models.Model):
    """教师表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('姓名', db_column='name', null=False, blank=False, default='', max_length=255)
    title = models.CharField('学位', db_column='title', null=False, blank=False, default='', max_length=255)
    duty = models.CharField('职位', db_column='duty', null=False, blank=False, default='', max_length=255)
    photo = models.ImageField('照片', db_column='photo', upload_to='teacherphoto', null=False, blank=False, default='')
    intro = models.TextField('简介', db_column='intro', null=True, blank=True)
    enabled = models.BooleanField('启用', db_column='enabled', null=False, blank=False, default=True)
    order_by = models.IntegerField('排序', db_column='order_by', null=True, blank=True, default=0)
    courses = models.ManyToManyField('Course', verbose_name='课程', related_name='CoursesOfTeacher',
                                     through='TeacherWithCourse', through_fields=('teacher', 'course'))
    courses1 = models.ManyToManyField('Course', verbose_name='课程', )
    class Meta:
        managed = True
        db_table = 'teacher'
        verbose_name = '教师'
        verbose_name_plural = '教师管理'

    def __str__(self):
        return self.name
