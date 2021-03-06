# Generated by Django 3.2.6 on 2021-09-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0005_auto_20210829_0513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'get_latest_by': 'id', 'verbose_name': '教师管理的课程', 'verbose_name_plural': '教师管理的课程'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'get_latest_by': 'id', 'verbose_name': '教师', 'verbose_name_plural': '教师'},
        ),
        migrations.AlterModelOptions(
            name='tutorial',
            options={'get_latest_by': 'id', 'verbose_name': '已发布的辅导', 'verbose_name_plural': '已发布的辅导'},
        ),
        migrations.AddField(
            model_name='course',
            name='describe',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='course',
            name='wallpaper',
            field=models.ImageField(blank=True, default='avatar.jpg', upload_to='avatar', verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar.jpg', upload_to='avatar', verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='location',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='默认地点'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='wechat_id',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='微信openid'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='describe',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='是否完成'),
        ),
    ]
