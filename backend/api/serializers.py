from datetime import date
from re import L
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from api.models import Shipment, ShippingCompany, Cargo
from api.validators import MinFieldLengthValidator, FloatFieldValidator


class CargoSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(
        validators=[MinFieldLengthValidator(
                    min_len=2, field_name='cargo name')])
    weight_kg = serializers.FloatField(
        validators=[FloatFieldValidator(field_name='Cargo weight (kg)')])
    volume_m3 = serializers.FloatField(
        validators=[FloatFieldValidator(field_name='Cargo volume (m3)')])

    class Meta:
        model = Cargo
        fields = ('id', 'name', 'weight_kg', 'volume_m3')


class ShipmentSerializer(WritableNestedModelSerializer):

    id = serializers.IntegerField(read_only=True)
    cargoes = CargoSerializer(many=True)

    recipient = serializers.CharField(
        validators=[MinFieldLengthValidator(
                    min_len=4, field_name='recipient')])
    destination = serializers.CharField(
        validators=[MinFieldLengthValidator(
                    min_len=4, field_name='destination')])
    description = serializers.CharField(
        validators=[MinFieldLengthValidator(
                    min_len=4, field_name='description')])

    class Meta:
        model = Shipment
        fields = ('__all__')

    def validate_ship_date(self, ship_date):
        if ship_date < date.today():
            raise serializers.ValidationError('The date has already passed')
        return ship_date

    def validate_cargoes(self, cargoes):
        if not cargoes:
            raise serializers.ValidationError('Please add at least one cargo')
        return cargoes


class ShippingCompanySerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    shipments = serializers.SlugRelatedField(many=True, read_only=True,
                                             slug_field='description')
    name = serializers.CharField(
        validators=[MinFieldLengthValidator(
                    min_len=4, field_name='shipping company name')])
    office = serializers.CharField(
        validators=[MinFieldLengthValidator(
                    min_len=4, field_name='office name')])
    contact = serializers.CharField(
        validators=[MinFieldLengthValidator(
                    min_len=4, field_name='contact name')])

    class Meta:
        model = ShippingCompany
        fields = ('id', 'name', 'office', 'contact',
                  'phone_number', 'shipments')
