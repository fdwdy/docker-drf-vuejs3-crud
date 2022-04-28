from dataclasses import field
from django.core.validators import RegexValidator
from rest_framework import serializers


phone_validator = RegexValidator(regex=r'^\+\d{9,15}$',
                                 message="Format:'+XXX' 9-15 digits.")


class MinFieldLengthValidator:

    def __init__(self, min_len, field_name):
        self.min_len = min_len
        self.field_name = field_name

    def __call__(self, value):
        if len(value) < self.min_len:
            raise serializers.ValidationError(
                'Min {} symbols for {}'.format(
                    self.min_len, self.field_name))
        return value


class FloatFieldValidator:

    def __init__(self, field_name):
        self.field_name = field_name

    def __call__(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                '{} must be greater than zero'.format(self.field_name))
        return value
