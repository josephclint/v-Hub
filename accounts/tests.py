from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

HTTP_OK = 200
HTTP_FOUND = 302


class UserRoutineTests(TestCase):

    @classmethod
    def setUpTestData(clazz):
        ''' test user details '''
        clazz.user_username = 'test_username'
        clazz.user_password = 'test_password'
        clazz.user_first_name = 'test_first_name'
        clazz.user_last_name = 'test_last_name'
        clazz.user_email = 'test@test.com'

    def test_user_registration_should_work_with_correct_inputs(self):
        # browse to the registration page
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, HTTP_OK)

        # register using the form (assuming the form is there)
        response = self.client.post(
            reverse('accounts:signup'),
            {
                'username': self.user_username,
                'password1': self.user_password,
                'password2': self.user_password,
                'email': self.user_email,
                'first_name': self.user_first_name,
                'last_name': self.user_last_name
            },
            follow=True
        )

        # make sure the user we just registered was really registered
        # username check is enough since it must be unique
        a = User.objects.filter(
            username=self.user_username,
        )
        self.assertTrue(a)

        # make sure it is logged in
        self.assertTrue(response.context['request'].user.is_authenticated())

    def test_user_login_should_work_with_existing_user(self):
        # create the test user
        User.objects.create_user(
            self.user_username,
            password=self.user_password
        )

        # browse to the login page
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, HTTP_OK)

        # login using the form
        response = self.client.post(
            reverse('accounts:login'),
            {
                'username': self.user_username,
                'password': self.user_password
            },
            follow=True
        )

        # make sure it successfully logged the test user in
        self.assertTrue(response.context['request'].user.is_authenticated())

    def test_user_login_should_not_work_with_nonexistent_user(self):
        pass

    def test_user_logout_should_work(self):
        # create the test user
        User.objects.create_user(
            self.user_username,
            password=self.user_password
        )

        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, HTTP_OK)
        self.assertFalse(response.context['request'].user.is_authenticated())
