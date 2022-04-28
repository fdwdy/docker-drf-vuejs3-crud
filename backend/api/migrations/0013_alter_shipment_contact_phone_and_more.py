# Generated by Django 4.0.3 on 2022-03-31 15:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_cargo_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='contact_phone',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Format:'+XXX' 9-15 digits.", regex='^\\+?1?\\d{9,15}$')], verbose_name="Recipient's phone"),
        ),
        migrations.AlterField(
            model_name='shippingcompany',
            name='phone_number',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Format:'+XXX' 9-15 digits.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Office phone number'),
        ),
    ]