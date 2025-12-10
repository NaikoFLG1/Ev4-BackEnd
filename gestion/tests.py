from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Company


class APISmokeTests(APITestCase):

	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='pass123')

		Company.objects.create(name='ACME', address='Av. Prueba 1', rut='12345678-9')

	def test_health_endpoint(self):
		resp = self.client.get('/api/health/')
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		self.assertEqual(resp.json().get('status'), 'ok')

	def test_anonymous_can_read_companies(self):
		resp = self.client.get('/api/companies/')
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		data = resp.json()
		self.assertTrue(isinstance(data, list) or 'results' in data)

	def test_authenticated_can_create_company(self):
		# obtener token
		token_resp = self.client.post('/api/auth/token/', {'username': 'testuser', 'password': 'pass123'}, format='json')
		self.assertEqual(token_resp.status_code, status.HTTP_200_OK)
		access = token_resp.json().get('access')
		self.assertIsNotNone(access)
		self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
		create_resp = self.client.post('/api/companies/', {'name': 'NewCo', 'address': 'Calle 2', 'rut': '98765432-1'}, format='json')
		self.assertEqual(create_resp.status_code, status.HTTP_201_CREATED)
