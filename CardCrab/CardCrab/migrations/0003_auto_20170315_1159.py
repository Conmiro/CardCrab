# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-15 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardCrab', '0002_auto_20170315_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='carddetails',
            name='format',
        ),
        migrations.AddField(
            model_name='carddetails',
            name='formats',
            field=models.ManyToManyField(to='CardCrab.PlayFormat'),
        ),
    ]