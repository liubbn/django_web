# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, verbose_name='\u6587\u7ae0\u6807\u9898')),
                ('snippet', models.CharField(default='\u8bf7\u70b9\u51fb\u67e5\u770b\u66f4\u8be6\u7ec6\u5185\u5bb9\u3002\u3002\u3002', max_length=500, verbose_name='\u6458\u8981')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('publish_time', models.DateTimeField(null=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('stats', models.CharField(default=b'd', max_length=1, verbose_name='\u6587\u7ae0\u72b6\u6001', choices=[(b'd', '\u8349\u7a3f'), (b'p', '\u53d1\u8868')])),
                ('is_public', models.BooleanField(default=True, verbose_name='\u516c\u5f00')),
                ('is_top', models.BooleanField(default=False, verbose_name='\u7f6e\u9876')),
                ('access_count', models.IntegerField(default=1, verbose_name='\u6d4f\u89c8\u91cf', editable=False)),
                ('author', models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish_time'],
                'verbose_name': '\u6587\u7ae0',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=150, verbose_name='\u5206\u7c7b\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=150, verbose_name='\u6807\u7b7e\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='MonthlyWeatherByCity',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='\u5206\u7c7b', to='blog.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='\u6807\u7b7e', blank=True),
            preserve_default=True,
        ),
    ]
