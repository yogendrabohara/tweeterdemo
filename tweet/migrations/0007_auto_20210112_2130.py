# Generated by Django 3.1.5 on 2021-01-13 05:30

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0006_auto_20210112_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='./djangopro/tweetdemo/media/photos'), upload_to=''),
        ),
    ]
