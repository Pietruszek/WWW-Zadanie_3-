# Generated by Django 2.0.5 on 2018-06-12 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airplanes_app', '0018_lot_zaloga'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zaloga',
            old_name='imie_nazwisko_kapitana',
            new_name='imie_i_nazwisko_kapitana',
        ),
    ]