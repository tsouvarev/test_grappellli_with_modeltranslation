# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 12:36
from __future__ import unicode_literals

from django.db import migrations


def make_tags(apps, schema_editor):
    Tag = apps.get_model('test_app', 'Tag')

    Tag.objects.bulk_create([
        Tag(name_en='en name', name_de='de name'),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(make_tags, migrations.RunPython.noop)
    ]
