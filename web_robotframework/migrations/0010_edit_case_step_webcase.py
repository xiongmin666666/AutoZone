# Generated by Django 2.1.1 on 2018-11-23 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_robotframework', '0009_remove_edit_case_step_webcase'),
    ]

    operations = [
        migrations.AddField(
            model_name='edit_case_step',
            name='Webcase',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web_robotframework.add_web_name'),
        ),
    ]
