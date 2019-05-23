# Generated by Django 2.1.1 on 2018-11-14 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_robotframework', '0002_auto_20181114_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_web_testcase',
            name='web_case_name',
            field=models.CharField(max_length=50, verbose_name='web测试名称'),
        ),
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webassertdata',
            field=models.CharField(max_length=200, verbose_name='验证数据'),
        ),
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webcomments',
            field=models.CharField(max_length=200, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webelement',
            field=models.CharField(max_length=800, verbose_name='控件元素'),
        ),
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webfindmethod',
            field=models.CharField(max_length=200, verbose_name='定位方式'),
        ),
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webopelement',
            field=models.CharField(max_length=200, verbose_name='操作方法'),
        ),
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webtestdata',
            field=models.CharField(max_length=200, verbose_name='测试数据'),
        ),
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webtestresult',
            field=models.BooleanField(verbose_name='测试结果'),
        ),
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webteststep',
            field=models.CharField(max_length=200, verbose_name='测试步骤'),
        ),
        migrations.AlterField(
            model_name='add_web_testcase',
            name='webteststepdesc',
            field=models.CharField(max_length=200, verbose_name='测试对象描述'),
        ),
    ]
