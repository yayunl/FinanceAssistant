# Generated by Django 2.0.6 on 2018-10-21 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0020_remove_bankstatementdocument_bank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankstatementdocument',
            name='file',
        ),
        migrations.AlterField(
            model_name='bankstatementdocument',
            name='owner',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
