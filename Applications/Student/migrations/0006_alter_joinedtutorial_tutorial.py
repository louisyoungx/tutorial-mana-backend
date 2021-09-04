# Generated by Django 3.2.6 on 2021-09-02 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0005_auto_20210829_0513'),
        ('Student', '0005_alter_joinedtutorial_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinedtutorial',
            name='tutorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.tutorial', verbose_name='辅导'),
        ),
    ]