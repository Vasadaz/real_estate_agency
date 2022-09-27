# Generated by Django 2.2.24 on 2022-09-14 18:20

from django.db import migrations


def identify_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    new_building_year = 2015

    Flat.objects.filter(
        construction_year__gte=new_building_year,
    ).update(
        new_building=True,
    )


def rollback(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20220914_1955'),
    ]

    operations = [
        migrations.RunPython(identify_new_building, rollback),
    ]
