# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0018_graphdata_value_avgbc'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphdata',
            name='value_avgBC1',
            field=models.DecimalField(default=1, verbose_name=b'   \xd0\x9f\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xbe\xd1\x82 0 - 50 \xd1\x81\xd0\xbc ', max_digits=6, decimal_places=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='graphdata',
            name='value_avgBC2',
            field=models.DecimalField(default=1, verbose_name=b'   \xd0\x9f\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xbe\xd1\x82 50 - 80 \xd1\x81\xd0\xbc ', max_digits=6, decimal_places=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='graphdata',
            name='value_avgBC3',
            field=models.DecimalField(default=1, verbose_name=b'   \xd0\x9f\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xbe\xd1\x82 80 \xd1\x81\xd0\xbc - 2 \xd0\xbc ', max_digits=6, decimal_places=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='graphdata',
            name='value_avgBC4',
            field=models.DecimalField(default=1, verbose_name=b'   \xd0\x9f\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9 \xd1\x81\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5 2 \xd0\xbc ', max_digits=6, decimal_places=3),
            preserve_default=False,
        ),
    ]
