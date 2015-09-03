# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150819_0045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publish_time'], 'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6240\u6709\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u5206\u7c7b\u4fe1\u606f', 'verbose_name_plural': '\u5206\u7c7b\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '\u6807\u7b7e', 'verbose_name_plural': '\u6807\u7b7e'},
        ),
    ]
