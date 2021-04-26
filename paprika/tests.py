from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagerTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='user1@tezt.com', password='user1passwd'
        )
        self.assertEqual(user.email, 'user1@tezt.com')
        self.assertTrue(user.check_password('user1passwd'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(ValueError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='user1passwd')

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            email='admin@tezt.com', password='adminpasswd'
        )
        self.assertEqual(user.email, 'admin@tezt.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_superuser(
                email='admin@tezt.com',
                password='adminpasswd',
                is_superuser=False,
            )
