# Generated by Django 3.1.1 on 2020-09-13 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200913_0939'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PermissionsMixin',
        ),
    ]