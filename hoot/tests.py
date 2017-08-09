import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import user
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_user(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["password"] = "password"
    defaults.update(**kwargs)
    return user.objects.create(**defaults)


class userViewTest(unittest.TestCase):
    '''
    Tests for user
    '''
    def setUp(self):
        self.client = Client()

    def test_list_user(self):
        url = reverse('hoot_user_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        url = reverse('hoot_user_create')
        data = {
            "name": "name",
            "password": "password",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_user(self):
        user = create_user()
        url = reverse('hoot_user_detail', args=[user.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        user = create_user()
        data = {
            "name": "name",
            "password": "password",
        }
        url = reverse('hoot_user_update', args=[user.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


