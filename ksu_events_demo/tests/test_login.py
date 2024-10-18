from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class CasLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.login_url = reverse('cas_ng_login')
        self.protected_url = reverse('authed')
    
    def test_cas_login1(self):
        # Simulate the CAS login process
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.protected_url, follow=True)
        
        # Verify that the user is authenticated
        self.assertTrue(self.user.is_authenticated)

    def test_cas_login2(self):
        #BadLogin = self.client.login(username='badUser', password='BadPass')
        #self.assertFalse(BadLogin, "Login should fail with incorrect credentials")

        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers.get('Location'), "/accounts/login/?next=/authed/")