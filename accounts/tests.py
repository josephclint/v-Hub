from django.core.urlresolvers import reverse_lazy
from django.test import TestCase
from django.contrib.auth.models import User


class UserOperationsTest(TestCase):

    def test_login_page(self):
        response = self.client.get(reverse_lazy('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('accounts/login.html' in [x.name for x in response.templates])

    def test_user_login(self):
        test_user = {
            'username': 'test_username',
            'password': 'test_password'
        }

        user = User.objects.create_user(test_user['username'], password=test_user['password'])
        user.save()

        response = self.client.login(username=test_user['username'], password=test_user['password'])
        self.assertTrue(response)

    def test_user_logout(self):
        test_user = {
            'username': 'test_username',
            'password': 'test_password'
        }

        user = User.objects.create_user(test_user['username'], password=test_user['password'])
        user.save()

        response = self.client.login(username=test_user['username'], password=test_user['password'])
        self.assertTrue(response)
        response = self.client.get(reverse_lazy('accounts:logout'))
        self.assertTrue('accounts/logout.html' in [x.name for x in response.templates])
