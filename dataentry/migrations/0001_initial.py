# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enter', models.DateTimeField(verbose_name=b'Enter')),
                ('exitt', models.DateTimeField(verbose_name=b'Exit')),
                ('today', models.DateField(verbose_name=b'Today')),
                ('week', models.IntegerField(default=1)),
                ('month', models.IntegerField(default=1)),
            ],
        ),
    ]
