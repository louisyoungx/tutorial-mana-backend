# Generated by Django 3.2.6 on 2021-08-28 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0002_alter_teacher_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
    ]
