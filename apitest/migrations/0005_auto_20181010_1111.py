# Generated by Django 2.1.1 on 2018-10-10 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0004_auto_20181010_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singel_apis',
            name='Apimethod',
            field=models.CharField(default='Get', max_length=20, verbose_name='请求方式'),
        ),
    ]
