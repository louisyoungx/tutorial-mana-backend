# Generated by Django 3.2.6 on 2021-09-02 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_alter_student_uid'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='joinedtutorial',
            table='joined_tutorial',
        ),
    ]