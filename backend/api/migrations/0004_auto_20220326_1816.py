# Generated by Django 4.0.3 on 2022-03-26 15:16

from django.db import migrations


class Migration(migrations.Migration):

    def link_cargos(apps, schema_editor):
        Shipment = apps.get_model('api', 'Shipment')
        Cargo = apps.get_model('api', 'Cargo')
        for shipment in Shipment.objects.all():
            Cargo.objects.create(name=shipment.cargo_text,
                                 weight=shipment.weight,
                                 volume=0, shipment=shipment)

    dependencies = [
        ('api', '0003_cargo_name'),
    ]

    operations = [
        migrations.RunPython(link_cargos),
    ]