# Generated by Django 2.1.1 on 2018-11-03 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0002_auto_20181103_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_apis_task',
            name='task_response',
            field=models.CharField(max_length=500, verbose_name='返回结果'),
        ),
        migrations.AlterField(
            model_name='singel_apis_task',
            name='task_response',
            field=models.CharField(max_length=500, verbose_name='返回结果'),
        ),
    ]
