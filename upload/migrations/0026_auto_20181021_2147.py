# Generated by Django 2.0.6 on 2018-10-21 21:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0025_auto_20181021_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankstatementdocument',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 21, 21, 47, 41, 668099), editable=False),
        ),
    ]