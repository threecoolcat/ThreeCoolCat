# Generated by Django 3.0.7 on 2020-08-15 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20200815_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinschool',
            name='course',
            field=models.ForeignKey(blank=True, db_column='course_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_courses', to='school.Course', verbose_name='课程'),
        ),
        migrations.AlterField(
            model_name='courseinschool',
            name='school',
            field=models.ForeignKey(blank=True, db_column='school_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_schools', to='school.School', verbose_name='校区'),
        ),
        migrations.CreateModel(
            name='TeacherWithCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(blank=True, db_column='course_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_courses', to='school.Course', verbose_name='课程')),
                ('teacher', models.ForeignKey(blank=True, db_column='teacher_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_teachers', to='school.Teacher', verbose_name='教师')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(through='school.TeacherWithCourse', to='school.Course', verbose_name='课程'),
        ),
    ]
