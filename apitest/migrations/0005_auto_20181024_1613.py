# Generated by Django 2.1.1 on 2018-10-24 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0004_auto_20181024_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singel_apis_task',
            name='task_id',
            field=models.AutoField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
