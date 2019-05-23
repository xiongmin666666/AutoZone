# Generated by Django 2.1.1 on 2018-11-21 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_robotframework', '0005_auto_20181121_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_case_step',
            name='Webcase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_robotframework.add_web_name'),
        ),
        migrations.AlterField(
            model_name='edit_case_step',
            name='webtest_step',
            field=models.CharField(max_length=200, verbose_name='测试步骤'),
        ),
    ]
