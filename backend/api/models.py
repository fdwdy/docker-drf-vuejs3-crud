from django.db import models
from api.validators import phone_validator


class Shipment(models.Model):
    shipping_company = models.ForeignKey("ShippingCompany", null=True,
                                         related_name='shipments',
                                         on_delete=models.CASCADE)
    recipient = models.CharField("Recipient", max_length=255, blank=False)
    destination = models.CharField("Destination address", max_length=255,
                                   blank=False)
    description = models.TextField("Description", max_length=500, blank=False)
    ship_date = models.DateField("Shipment date")
    contact_phone = models.CharField("Recipient's phone",
                                     validators=[phone_validator],
                                     max_length=17, blank=False)


class ShippingCompany(models.Model):
    name = models.CharField("Name", max_length=255, blank=False)
    office = models.CharField("Office address", max_length=255, blank=False)
    contact = models.CharField("Contact person", max_length=255, blank=False)
    phone_number = models.CharField("Office phone number",
                                    validators=[phone_validator],
                                    max_length=17, blank=False)


class Cargo(models.Model):
    name = models.CharField(max_length=255, blank=False)
    shipment = models.ForeignKey("Shipment", on_delete=models.CASCADE,
                                 null=True, related_name='cargoes')
    weight_kg = models.FloatField("Cargo weight, kg")
    volume_m3 = models.FloatField("Cargo volume, cubic m")
