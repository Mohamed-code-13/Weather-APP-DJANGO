# Generated by Django 3.0.5 on 2020-05-19 03:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0004_auto_20200519_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 3, 13, 38, 626672, tzinfo=utc)),
        ),
    ]
