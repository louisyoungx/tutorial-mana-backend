# Generated by Django 3.2.6 on 2021-09-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0006_auto_20210905_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='wallpaper',
            field=models.ImageField(blank=True, default='wallpaper.jpg', upload_to='wallpaper', verbose_name='背景'),
        ),
    ]