# Generated by Django 2.0.1 on 2018-02-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HANAPP', '0015_auto_20180202_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers2',
            name='Time1',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teachers2',
            name='Time2',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teachers2',
            name='Time3',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teachers2',
            name='Time4',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teachers2',
            name='Time5',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
