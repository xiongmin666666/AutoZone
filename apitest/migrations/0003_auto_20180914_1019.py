# Generated by Django 2.1.1 on 2018-09-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0002_auto_20180913_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_product',
            name='status',
            field=models.CharField(max_length=20, verbose_name='是否通过'),
        ),
    ]
