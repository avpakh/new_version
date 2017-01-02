# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0028_auto_20160228_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestData',
            fields=[
                ('id_table', models.AutoField(serialize=False, primary_key=True)),
                ('id_station', models.SmallIntegerField(verbose_name=b'ID_STATION')),
                ('dt_observation', models.DateTimeField(verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81/\xd0\x94\xd0\xb5\xd0\xbd\xd1\x8c')),
                ('date_observation', models.DateField(verbose_name=b'DATA_OBS')),
                ('value_min', models.DecimalField(verbose_name=b'   \xd0\x9c\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb7\xd0\xb0 \xd1\x81\xd1\x83\xd1\x82\xd0\xba\xd0\xb8   ', max_digits=6, decimal_places=2)),
                ('value_max', models.DecimalField(verbose_name=b'   \xd0\x9c\xd0\xb0\xd0\xba\xd1\x81\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb7\xd0\xb0 \xd1\x81\xd1\x83\xd1\x82\xd0\xba\xd0\xb8   ', max_digits=6, decimal_places=2)),
                ('value_avg', models.DecimalField(verbose_name=b'   \xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xbe\xd1\x82 \xd0\xbe\xd1\x82\xd0\xbc\xd0\xb5\xd1\x82\xd0\xba\xd0\xb8 0 \xd1\x81\xd1\x82\xd0\xb0\xd0\xbd\xd1\x86\xd0\xb8\xd0\xb8 \xd0\x90\xd0\x93\xd0\xa1 (\xd1\x81\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbd\xd0\xb5\xd0\xb5 \xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb7\xd0\xb0 \xd1\x81\xd1\x83\xd1\x82\xd0\xba\xd0\xb8)', max_digits=6, decimal_places=2)),
                ('value_avgBC', models.DecimalField(null=True, verbose_name=b' \xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xb4\xd0\xbe \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb8', max_digits=6, decimal_places=3)),
                ('value_avgBC1', models.DecimalField(null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xb4\xd0\xbe 50 \xd1\x81\xd0\xbc', max_digits=6, decimal_places=3)),
                ('value_avgBC2', models.DecimalField(null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xb4\xd0\xbe 80 \xd1\x81\xd0\xbc', max_digits=6, decimal_places=3)),
                ('value_avgBC3', models.DecimalField(null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xb4\xd0\xbe 2 \xd0\xbc', max_digits=6, decimal_places=3)),
                ('value_avgBC4', models.DecimalField(null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9 \xd1\x81\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5 2 \xd0\xbc', max_digits=6, decimal_places=3)),
                ('value_avgBC50', models.DecimalField(null=True, verbose_name=b'\xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c - 50 \xd1\x81\xd0\xbc \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9', max_digits=6, decimal_places=3)),
                ('value_avgBC60', models.DecimalField(null=True, verbose_name=b'\xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xb4\xd0\xbe \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb8', max_digits=6, decimal_places=3)),
            ],
            options={
                'db_table': 'RequestData',
            },
        ),
        migrations.AlterField(
            model_name='requestav',
            name='value_avg',
            field=models.DecimalField(verbose_name=b'    \xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xbe\xd1\x82 \xd0\xbe\xd1\x82\xd0\xbc\xd0\xb5\xd1\x82\xd0\xba\xd0\xb8 0 \xd1\x81\xd1\x82\xd0\xb0\xd0\xbd\xd1\x86\xd0\xb8\xd0\xb8 \xd0\x90\xd0\x93\xd0\xa1 (\xd1\x81\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbd\xd0\xb5\xd0\xb5 \xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb7\xd0\xb0 \xd1\x81\xd1\x83\xd1\x82\xd0\xba\xd0\xb8)  ', max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requestav',
            name='value_max',
            field=models.DecimalField(verbose_name=b'    \xd0\x9c\xd0\xb0\xd0\xba\xd1\x81\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb7\xd0\xb0 \xd1\x81\xd1\x83\xd1\x82\xd0\xba\xd0\xb8  ', max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requestav',
            name='value_min',
            field=models.DecimalField(verbose_name=b'    \xd0\x9c\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb7\xd0\xb0 \xd1\x81\xd1\x83\xd1\x82\xd0\xba\xd0\xb8   ', max_digits=6, decimal_places=2),
        ),
    ]
