# Generated by Django 2.2.1 on 2019-05-26 03:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0037_auto_20190525_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 26, 0, 1, 42, 997964)),
        ),
    ]
