# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HourEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('notes', models.TextField()),
                ('pub_date', models.DateField(verbose_name='Date Worked')),
                ('hours', models.DecimalField(decimal_places=2, blank=True, null=True, max_digits=5)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('billable', models.BooleanField(default=False)),
                ('billed', models.BooleanField(default=False)),
                ('name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'hour entries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('project', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ('project',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='hourentry',
            name='project',
            field=models.ForeignKey(to='merkhet.Project'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('task', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ('task',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='hourentry',
            name='task',
            field=models.ForeignKey(to='merkhet.Task'),
            preserve_default=True,
        ),
    ]
