import json
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Cargo, Shipment
from api.serializers import ShipmentSerializer


client = APIClient()

class ShipmentsTest(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(ShipmentsTest, cls).setUpClass()

        cls.valid_payload = {
            "cargoes": [{"name": "cargo", "weight_kg": 12, "volume_m3": 3}],
            "recipient": "recipient",
            "contact_phone": "+37544444444",
            "destination": "destination_new",
            "description": "description_new",
            "ship_date": "2024-03-02"
        }

        cls.invalid_payload = {
            "cargoes": [{"name": "cargo", "weight_kg": 12, "volume_m3": 3}],
            "contact_phone": "+37544444444",
            "destination": "destination_invalid",
            "description": "description_invalid",
            "ship_date": "2024-03-02"
        }

        cls.shipment = Shipment.objects.create(recipient="sdf",
                                           destination="destination",
                                           description="description",
                                           ship_date="2022-03-02",
                                           contact_phone="+37544444444")
        cargo = Cargo.objects.create(name="crg", weight_kg=12, volume_m3=3)
        cls.shipment.cargoes.set([cargo])

    def test_should_return_all_shipments(self):
        response = client.get(reverse('shipment-list'))
        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(len(shipments), 1)

    def test_should_return_shipment_by_id(self):
        response = client.get(
            reverse('shipment-detail', kwargs={'pk': self.shipment.id}))
        shipment = Shipment.objects.get(pk=self.shipment.id)
        serializer = ShipmentSerializer(shipment)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_get_non_existent_shipment_should_fail(self):
        response = client.get(
            reverse('shipment-detail', kwargs={'pk': 8888}))
        error_message = response.data.get('detail', None)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(error_message, 'Not found.')

    def test_should_create_shipment_with_valid_payload(self):
        response = client.post(
            reverse('shipment-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        shipment_id = response.data.get('id')
        shipment = Shipment.objects.get(pk=shipment_id)
        shipments = Shipment.objects.all()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(shipment.description, self.valid_payload.get('description'))
        self.assertEqual(len(shipments), 2)

    def test_create_shipment_with_invalid_payload_should_fail(self):
        response = client.post(
            reverse('shipment-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        shipments = Shipment.objects.all()
        error_message = response.data.get('recipient', None)[0]

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error_message, 'This field is required.')
        self.assertEqual(len(shipments), 1)

    def test_should_update_shipment_with_valid_payload(self):
        response = client.put(
            reverse('shipment-detail', kwargs={'pk': self.shipment.id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        shipment = Shipment.objects.get(pk=self.shipment.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(shipment.description, 'description_new')

    def test_update_shipment_with_invalid_payload_should_fail(self):
        response = client.put(
            reverse('shipment-detail', kwargs={'pk': self.shipment.id}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        shipment = Shipment.objects.get(pk=self.shipment.id)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(shipment.description, 'description_invalid')

    def test_should_delete_shipment(self):
        response = client.delete(
            reverse('shipment-detail', kwargs={'pk': self.shipment.id}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Shipment.DoesNotExist):
            Shipment.objects.get(id=self.shipment.id)

    def test_delete_non_existent_shipment_should_fail(self):
        response = client.delete(
            reverse('shipment-detail', kwargs={'pk': 8888}))
        error_message = response.data.get('detail', None)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(error_message, 'Not found.')
