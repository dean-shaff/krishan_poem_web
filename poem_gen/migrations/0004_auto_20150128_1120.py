# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poem_gen', '0003_auto_20150123_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinput',
            name='text',
            field=models.FileField(upload_to=b'/home/dean/python_stuff_ubuntu/web/poem_maker/media/texts'),
            preserve_default=True,
        ),
    ]
