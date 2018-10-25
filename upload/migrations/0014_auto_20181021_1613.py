# Generated by Django 2.0.6 on 2018-10-21 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0013_bankstatement_bank_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankStatementDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='doc/')),
                ('bank', models.CharField(blank=True, max_length=50)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]