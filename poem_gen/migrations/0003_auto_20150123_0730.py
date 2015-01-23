# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import poem_gen.models


class Migration(migrations.Migration):

    dependencies = [
        ('poem_gen', '0002_textinput_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinput',
            name='text',
            field=models.FileField(upload_to=poem_gen.models.get_file_path),
            preserve_default=True,
        ),
    ]
