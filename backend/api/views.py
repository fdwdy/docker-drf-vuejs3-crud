from rest_framework.viewsets import ModelViewSet

from api.models import Shipment, ShippingCompany
from api.serializers import ShipmentSerializer, ShippingCompanySerializer


class ShipmentViewSet(ModelViewSet):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()


class ShippingCompanyViewSet(ModelViewSet):
    serializer_class = ShippingCompanySerializer
    queryset = ShippingCompany.objects.all()
