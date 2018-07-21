# Generated by Django 2.0.1 on 2018-01-17 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HANAPP', '0004_auto_20180117_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers2',
            name='AVAILABILITY',
            field=models.CharField(choices=[('AVAIL', 'AVAILABLE'), ('UNAVAIL', 'UNAVAILABLE')], default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teachers2',
            name='STATUS',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
