# Generated by Django 3.0.7 on 2020-08-15 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20200624_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', default='', max_length=255, verbose_name='姓名')),
                ('title', models.CharField(db_column='title', default='', max_length=255, verbose_name='学位')),
                ('duty', models.CharField(db_column='duty', default='', max_length=255, verbose_name='职位')),
                ('photo', models.ImageField(db_column='photo', default='', max_length=255, upload_to='', verbose_name='职位')),
                ('intro', models.TextField(blank=True, db_column='intro', null=True, verbose_name='简介')),
                ('enabled', models.BooleanField(db_column='enabled', default=True, verbose_name='启用')),
                ('order_by', models.IntegerField(blank=True, db_column='order_by', default=0, null=True, verbose_name='排序')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师管理',
                'db_table': 'teacher',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'managed': True, 'verbose_name': '课程', 'verbose_name_plural': '课程管理'},
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.IntegerField(blank=True, choices=[(1, '线下课程'), (2, '线上课程')], db_column='category', default=1, null=True, verbose_name='类别'),
        ),
        migrations.AddField(
            model_name='school',
            name='enabled',
            field=models.BooleanField(db_column='enabled', default=True, verbose_name='启用'),
        ),
    ]
