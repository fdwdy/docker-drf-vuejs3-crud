# Generated by Django 4.0.3 on 2022-04-14 07:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_shipment_contact_phone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo',
            old_name='volume',
            new_name='volume_m3',
        ),
        migrations.RenameField(
            model_name='cargo',
            old_name='weight',
            new_name='weight_kg',
        ),
        migrations.AlterField(
            model_name='cargo',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='contact_phone',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Format:'+XXX' 9-15 digits.", regex='^\\+\\d{9,15}$')], verbose_name="Recipient's phone"),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='destination',
            field=models.CharField(max_length=255, verbose_name='Destination address'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='recipient',
            field=models.CharField(max_length=255, verbose_name='Recipient'),
        ),
        migrations.AlterField(
            model_name='shippingcompany',
            name='contact',
            field=models.CharField(max_length=255, verbose_name='Contact person'),
        ),
        migrations.AlterField(
            model_name='shippingcompany',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='shippingcompany',
            name='office',
            field=models.CharField(max_length=255, verbose_name='Office address'),
        ),
        migrations.AlterField(
            model_name='shippingcompany',
            name='phone_number',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Format:'+XXX' 9-15 digits.", regex='^\\+\\d{9,15}$')], verbose_name='Office phone number'),
        ),
    ]