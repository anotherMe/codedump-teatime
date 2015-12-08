# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import teatime.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=teatime.models.get_pin_path)),
                ('isCoverImage', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('altName', models.CharField(max_length=200, verbose_name=b'alternative name')),
                ('descr', models.TextField(verbose_name=b'Description')),
                ('rating', models.IntegerField(default=0)),
                ('addDate', models.DateField(verbose_name=b'date added')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sample',
            name='shop',
            field=models.ForeignKey(to='teatime.Shop'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pin',
            name='sample',
            field=models.ForeignKey(to='teatime.Sample'),
            preserve_default=True,
        ),
    ]
