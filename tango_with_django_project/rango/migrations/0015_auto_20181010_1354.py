# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-10-10 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0014_auto_20181008_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='file',
            field=models.FileField(blank=True, upload_to='upload_file_from_page'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]
