# Generated by Django 2.0.6 on 2018-10-21 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0022_auto_20181021_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankstatementdocument',
            name='file',
            field=models.FileField(blank=True, upload_to='doc/'),
        ),
    ]