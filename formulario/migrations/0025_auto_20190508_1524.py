# Generated by Django 2.2.1 on 2019-05-08 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0024_auto_20190508_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 8, 15, 24, 36, 587353)),
        ),
    ]
