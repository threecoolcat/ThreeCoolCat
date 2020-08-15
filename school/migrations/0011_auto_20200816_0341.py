# Generated by Django 3.0.7 on 2020-08-16 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_auto_20200816_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(to='school.Course', verbose_name='课程'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(db_column='photo', default='', upload_to='teacherphoto', verbose_name='照片'),
        ),
    ]