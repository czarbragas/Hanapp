# Generated by Django 2.0 on 2018-01-01 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITAssetManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='fname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='lname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]