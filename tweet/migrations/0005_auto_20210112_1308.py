# Generated by Django 3.1.5 on 2021-01-12 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0004_auto_20210110_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
