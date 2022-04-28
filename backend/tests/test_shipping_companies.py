import json
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import ShippingCompany
from api.serializers import ShippingCompanySerializer


client = APIClient()

class CompaniesTest(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(CompaniesTest, cls).setUpClass()

        cls.valid_payload = {
            "name": "name_new",
            "office": "office_new",
            "contact": "contact_new",
            "phone_number": "+5895233342"
        }

        cls.invalid_payload = {
            "office": "office_new",
            "contact": "contact",
            "phone_number": "+5895233342"
        }

        cls.company = ShippingCompany.objects.create(name="name", office="office",
                                       contact="contact",
                                       phone_number="+5895233342")

    def test_should_return_all_companies(self):
        response = client.get(reverse('shippingcompany-list'))
        companies = ShippingCompany.objects.all()
        serializer = ShippingCompanySerializer(companies, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(len(companies), 1)

    def test_should_return_company_by_id(self):
        response = client.get(
            reverse('shippingcompany-detail', kwargs={'pk': self.company.id}))
        company = ShippingCompany.objects.get(pk=self.company.id)
        serializer = ShippingCompanySerializer(company)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_get_non_existent_company_should_fail(self):
        response = client.get(
            reverse('shippingcompany-detail', kwargs={'pk': 8888}))
        error_message = response.data.get('detail', None)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(error_message, 'Not found.')

    def test_should_create_company_with_valid_payload(self):
        response = client.post(
            reverse('shippingcompany-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        company_id = response.data.get('id')
        company = ShippingCompany.objects.get(pk=company_id)
        companies = ShippingCompany.objects.all()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(company.name, self.valid_payload.get('name'))
        self.assertEqual(len(companies), 2)

    def test_create_company_with_invalid_payload_should_fail(self):
        response = client.post(
            reverse('shippingcompany-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        companies = ShippingCompany.objects.all()
        error_message = response.data.get('name', None)[0]

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error_message, 'This field is required.')
        self.assertEqual(len(companies), 1)

    def test_should_update_company_with_valid_payload(self):
        response = client.put(
            reverse('shippingcompany-detail', kwargs={'pk': self.company.id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        company = ShippingCompany.objects.get(pk=self.company.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(company.name, 'name_new')

    def test_update_company_with_invalid_payload_should_fail(self):
        response = client.put(
            reverse('shippingcompany-detail', kwargs={'pk': self.company.id}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        company = ShippingCompany.objects.get(pk=self.company.id)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(company.office, 'office_new')

    def test_should_delete_company(self):
        response = client.delete(
            reverse('shippingcompany-detail', kwargs={'pk': self.company.id}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(ShippingCompany.DoesNotExist):
            ShippingCompany.objects.get(id=self.company.id)

    def test_delete_non_existent_company_should_fail(self):
        response = client.delete(
            reverse('shippingcompany-detail', kwargs={'pk': 8888}))
        error_message = response.data.get('detail', None)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(error_message, 'Not found.')
