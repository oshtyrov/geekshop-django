# Generated by Django 2.2.17 on 2021-03-21 19:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210317_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 23, 19, 16, 13, 20746, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.SmallIntegerField(blank=True, default=18, null=True),
        ),
    ]
