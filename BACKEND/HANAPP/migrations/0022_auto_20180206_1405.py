# Generated by Django 2.0.1 on 2018-02-06 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HANAPP', '0021_auto_20180206_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers2',
            name='STATUS',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teachers2',
            name='Time1',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='teachers2',
            name='Time2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='teachers2',
            name='Time3',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='teachers2',
            name='Time4',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='teachers2',
            name='Time5',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
