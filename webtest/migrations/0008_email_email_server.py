# Generated by Django 2.1.5 on 2019-01-18 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0007_auto_20190116_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='email_server',
            field=models.CharField(default='', max_length=20),
        ),
    ]
