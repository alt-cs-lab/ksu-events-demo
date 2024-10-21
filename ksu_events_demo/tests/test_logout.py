from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class CasLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.logout_url = reverse('cas_ng_logout')
        self.login_url = reverse('cas_ng_login')
        self.protected_url = reverse('authed')
    
    #Tests login and logout proceedure, makes sure once logged out we redirect to login page
    def test_cas_logout1(self):
        # Login
        self.client.login(username='testuser', password='testpass')

        response = self.client.get(self.logout_url) 

        # Check if the response is a redirect, which means the logout was successful
        self.assertEqual(response.status_code, 302)

        # Verify that the user is not in the current session
        self.assertFalse(self.user in self.client.session)


        response = self.client.get(self.protected_url)

        #Should redirect to login page
        self.assertEqual(response.status_code, 302)

        #Response should let us know we are moving to login page
        self.assertEqual(response.headers.get('Location'), "/accounts/login/?next=/authed/")

