# Generated by Django 2.0.5 on 2018-06-12 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airplanes_app', '0015_remove_lot_zaloga'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Zaloga',
        ),
    ]
