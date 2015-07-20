from django.test import TestCase

from django.contrib.auth.models import User


HTTP_OK = 200
HTTP_FOUND = 302


class UserRoutineTests():

    @classmethod
    def setUpTestData(clazz):
        ''' test user details '''
        clazz.user_username = 'test_username'
        clazz.user_password = 'test_password'
        clazz.user_first_name = 'test_first_name'
        clazz.user_last_name = 'test_last_name'
        clazz.user_email = 'test@test.com'

    def test_user_registration_should_work(self):
        # browse to the registration page
        request = self.client.get(reverse('accounts:signup'))
        self.assertEqual(request.STATUS_CODE, HTTP_OK)

        # register using the form (assuming the form is there)
        request = self.client.post(
            reverse('accounts:signup'),
            {
                'username': self.user_username,
                'password1': self.user_password,
                'password2': self.user_password,
                'email': self.user_email,
                'first_name': self.user_first_name,
                'last_name': self.user_last_name
            },
            follow=True,
        )

        # make sure everything is OK
        for redirection in request.request_chain:
            self.assertEqual(redirection[1], HTTP_FOUND)

        # make sure the user we just registered was really registered
        # username check is enough since it must be unique
        a = User.objects.filter(
            username=self.user_username,
        )
        self.assertTrue(a)

        # make sure it is logged in
        self.assertTrue(request.user.is_authenticated())
