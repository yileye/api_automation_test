# Generated by Django 2.0.2 on 2018-02-09 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0010_auto_20180209_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmember',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_project', to='api_test.Project', verbose_name='所属项目'),
        ),
    ]