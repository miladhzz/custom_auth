# Generated by Django 3.0.8 on 2020-07-10 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneregister', '0002_auto_20200710_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='otp_create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 10, 22, 4, 32, 182848)),
        ),
    ]
