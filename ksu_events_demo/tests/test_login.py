from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class CasLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.login_url = reverse('cas_ng_login')
        self.protected_url = reverse('authed')


    #This block of code should mock if login is successful, and that the authed path is reachable
    def test_cas_login1(self):
        #Login with valid credentials
        self.client.login(username='testuser', password='password')

        #Checks to see if login was authenticated
        self.assertTrue(self.user.is_authenticated)

        response = self.client.get(self.protected_url)

        #Checks to see if authed is a valid path to reach once logged in
        self.assertEqual(response.request['PATH_INFO'], "/authed/")

    #Block of code should not be logged in and make sure that we are redirected to login page
    def test_cas_login2(self):
        response = self.client.get(self.protected_url)

        #Should redirect to login page
        self.assertEqual(response.status_code, 302)

        #Response should let us know we are moving to login page
        self.assertEqual(response.headers.get('Location'), "/accounts/login/?next=/authed/")