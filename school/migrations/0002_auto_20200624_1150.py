# Generated by Django 3.0.7 on 2020-06-24 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', default='', max_length=255, verbose_name='名称')),
                ('intro', models.TextField(blank=True, db_column='intro', null=True, verbose_name='简介')),
                ('enabled', models.BooleanField(db_column='enabled', default=True, verbose_name='启用')),
                ('order_by', models.IntegerField(blank=True, db_column='order_by', default=0, null=True, verbose_name='排序')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品管理',
                'db_table': 'course',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CourseInSchool',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(blank=True, db_column='course_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='school.Course', verbose_name='课程')),
                ('school', models.ForeignKey(blank=True, db_column='school_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='school.School', verbose_name='校区')),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='courses',
            field=models.ManyToManyField(through='school.CourseInSchool', to='school.Course', verbose_name='课程'),
        ),
    ]
