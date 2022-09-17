# Generated by Django 2.2.24 on 2022-09-17 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20220917_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaint',
            options={'verbose_name': 'жалобу', 'verbose_name_plural': 'Жалобы'},
        ),
        migrations.AlterModelOptions(
            name='flat',
            options={'verbose_name': 'квартиру', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AlterModelOptions(
            name='owner',
            options={'verbose_name': 'собственника', 'verbose_name_plural': 'Собственники'},
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
