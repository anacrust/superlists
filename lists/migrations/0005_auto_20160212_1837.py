# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import lists.models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20160212_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.TextField(verbose_name=lists.models.List, default=None),
        ),
    ]
