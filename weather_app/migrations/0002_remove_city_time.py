# Generated by Django 2.2.5 on 2019-12-22 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='time',
        ),
    ]
