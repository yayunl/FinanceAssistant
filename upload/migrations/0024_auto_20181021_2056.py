# Generated by Django 2.0.6 on 2018-10-22 01:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0023_bankstatementdocument_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankstatementdocument',
            name='slug',
            field=models.SlugField(blank=True, max_length=63, unique=True),
        ),
        migrations.AddField(
            model_name='bankstatementdocument',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 22, 1, 56, 52, 29825, tzinfo=utc), editable=False),
        ),
    ]