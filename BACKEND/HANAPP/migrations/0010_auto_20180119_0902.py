# Generated by Django 2.0.1 on 2018-01-19 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HANAPP', '0009_auto_20180119_0725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachers2',
            old_name='ProfPic',
            new_name='ProfPicAngry',
        ),
        migrations.AddField(
            model_name='teachers2',
            name='ProfPicHappy',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
