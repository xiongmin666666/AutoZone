# Generated by Django 2.1.1 on 2018-11-07 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0003_auto_20181103_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='need_data_apis',
            name='Apiparameter',
        ),
        migrations.RemoveField(
            model_name='process_apis_task',
            name='task_Apiparameter',
        ),
        migrations.RemoveField(
            model_name='singel_apis',
            name='Apiparameter',
        ),
        migrations.RemoveField(
            model_name='singel_apis_task',
            name='task_Apiparameter',
        ),
    ]
