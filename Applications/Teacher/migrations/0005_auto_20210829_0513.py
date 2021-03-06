# Generated by Django 3.2.6 on 2021-08-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0004_alter_teacher_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='nums',
            field=models.IntegerField(default=0, verbose_name='参加人数'),
        ),
        migrations.AlterField(
            model_name='course',
            name='limit',
            field=models.IntegerField(default=0, verbose_name='人数限制'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='joined_num',
            field=models.IntegerField(default=0, verbose_name='已加入人数'),
        ),
    ]
