# Generated by Django 3.1 on 2020-10-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0016_auto_20201002_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'teacher_courses',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='teacher',
            name='keyword',
            field=models.CharField(blank=True, db_column='keyword', default='', max_length=255, null=True, verbose_name='关键词'),
        ),
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(through='school.TeacherCourses', to='school.Teacher'),
        ),
    ]
