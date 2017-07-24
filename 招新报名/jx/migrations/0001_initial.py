# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('result', models.CharField(max_length=300)),
                ('problem', models.CharField(max_length=300)),
                ('zj', models.CharField(max_length=300)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
