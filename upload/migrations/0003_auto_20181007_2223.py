# Generated by Django 2.0.6 on 2018-10-08 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20181007_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankstatement',
            name='post_date',
            field=models.CharField(blank=True, max_length=30, verbose_name='Post Date'),
        ),
    ]
