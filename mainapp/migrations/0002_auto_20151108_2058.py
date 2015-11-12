# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('absenceStudent', models.ForeignKey(to='mainapp.Student')),
                ('lesson', models.ForeignKey(to='mainapp.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('info', models.CharField(max_length=200)),
                ('lesson', models.ForeignKey(to='mainapp.Lesson')),
                ('remarkStudent', models.ForeignKey(to='mainapp.Student')),
            ],
        ),
        migrations.RemoveField(
            model_name='admin',
            name='user',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]
