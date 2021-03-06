# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
        ('scraping', '0002_auto_20161008_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemporaryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_availability', models.CharField(blank=True, max_length=255, verbose_name='Shop availibility')),
                ('shop_code', models.CharField(blank=True, max_length=20, verbose_name='Shop code')),
                ('shop_title', models.CharField(blank=True, max_length=255, verbose_name='Shop title')),
                ('search_title', models.CharField(blank=True, max_length=255, verbose_name='Search title')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('shop_url', models.URLField(blank=True, verbose_name='Shop URL')),
                ('shop_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Shop price')),
                ('shop_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.ShopCategory')),
            ],
            options={
                'db_table': 'tempitems',
                'verbose_name': 'Temporary item',
                'verbose_name_plural': 'Temporary items',
            },
        ),
    ]
