# Generated by Django 2.1.1 on 2018-11-23 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_robotframework', '0010_edit_case_step_webcase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_case_step',
            name='Webcase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_robotframework.add_web_name'),
        ),
    ]
