# Generated by Django 2.2.1 on 2019-05-08 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0011_auto_20190508_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 8, 13, 38, 24, 373862)),
        ),
    ]
