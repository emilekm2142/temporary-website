# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('js', models.TextField()),
                ('css', models.TextField()),
                ('html', models.TextField()),
                ('name', models.TextField()),
                ('viewsCount', models.IntegerField()),
                ('usesBoostrap', models.BooleanField(default=False)),
                ('usesJquery', models.BooleanField(default=False)),
                ('endingDate', models.DateTimeField()),
                ('hash', models.TextField()),
                ('isPrivate', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
