# Generated by Django 2.0.1 on 2018-01-16 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HANAPP', '0002_auto_20180115_0846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachers2',
            name='username',
        ),
    ]
