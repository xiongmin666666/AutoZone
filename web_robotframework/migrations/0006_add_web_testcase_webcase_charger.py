# Generated by Django 2.1.1 on 2018-11-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_robotframework', '0005_add_web_testcase_webcase_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_web_testcase',
            name='webcase_charger',
            field=models.CharField(default=None, max_length=200, verbose_name='负责人'),
        ),
    ]
