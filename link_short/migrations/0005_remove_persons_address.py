# Generated by Django 3.0.4 on 2020-06-25 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link_short', '0004_auto_20200625_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persons',
            name='address',
        ),
    ]
