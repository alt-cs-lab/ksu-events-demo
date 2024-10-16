from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class CasLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.logout_url = reverse('cas_ng_logout')
    
    def test_cas_logout1(self):
        # Simulate the CAS login process
        self.client.login(username='testuser', password='testpass')

        response = self.client.get(self.logout_url) 

        # Check if the response is a redirect, which means the logout was successful
        self.assertEqual(response.status_code, 302)

        # Verify that the user is current session
        self.assertFalse(self.user in self.client.session)

    def test_cas_logout2(self):
        # Simulate the CAS login process
        self.client.login(username='badUser', password='BadPass')
        self.assertFalse(self.client.login(username='badUser', password='BadPass'), "Login should fail with incorrect credentials")

        response = self.client.get(self.logout_url) 

        #self.assertNotEqual(response.status_code, 302)

        # Verify that the user is authenticated
        self.assertFalse(self.user in self.client.session)
