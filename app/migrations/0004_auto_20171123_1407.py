# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-23 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171123_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='img_path',
            field=models.CharField(default='/static/img/blog/view1.jpg', max_length=256),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='body',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
