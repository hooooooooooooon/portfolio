# Generated by Django 4.2.5 on 2023-09-29 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_remove_work_theme_work_kind_alter_work_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='kind',
        ),
    ]
