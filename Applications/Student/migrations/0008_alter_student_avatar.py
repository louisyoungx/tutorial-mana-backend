# Generated by Django 3.2.6 on 2021-09-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0007_auto_20210905_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.URLField(blank=True, default='http://www.louisyoung.site:8002/TutorialManage/avatar.jpg', verbose_name='头像'),
        ),
    ]
