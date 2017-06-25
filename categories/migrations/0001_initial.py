# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text="Used to build the category's URL.", max_length=255, unique=True, verbose_name='slug')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='categories.Category', verbose_name='parent category')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]
