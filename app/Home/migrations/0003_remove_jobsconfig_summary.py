# Generated by Django 4.0.2 on 2022-02-14 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_homemodel_jobsconfig'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobsconfig',
            name='summary',
        ),
    ]
