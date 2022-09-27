# Generated by Django 2.2.24 on 2022-09-16 18:20

from django.db import migrations


def move_flat_owners_to_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.iterator():
        owner, created = Owner.objects.get_or_create(
            owner=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone,
        )
        owner.flats.add(flat)


def rollback(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Owner.objects.delete()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0011_owner'),
    ]

    operations = [
        migrations.RunPython(move_flat_owners_to_owner, rollback),
    ]
