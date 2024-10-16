from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class CasLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.login_url = reverse('cas_ng_login')
    
    def test_cas_login(self):
        # Simulate the CAS login process
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpass'})
        
        # Check if the response is a redirect, which means the login was successful
        self.assertEqual(response.status_code, 302)

        # Verify that the user is authenticated
        self.assertTrue(self.user.is_authenticated)

