# Generated by Django 2.0.6 on 2018-10-08 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(verbose_name='Trans. Date')),
                ('post_date', models.DateTimeField(verbose_name='Post Date')),
                ('transaction_amount', models.FloatField(verbose_name='Amount')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('category', models.CharField(blank=True, max_length=30, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='doc/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]