# Generated by Django 3.1 on 2020-08-26 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20200816_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True, db_column='start_date', null=True, verbose_name='开课时间'),
        ),
        migrations.AlterField(
            model_name='course',
            name='period',
            field=models.CharField(blank=True, db_column='period', max_length=100, null=True, verbose_name='单课时长'),
        ),
        migrations.AlterField(
            model_name='course',
            name='period_amount',
            field=models.CharField(blank=True, db_column='period_amount', max_length=100, null=True, verbose_name='学习周期'),
        ),
    ]
