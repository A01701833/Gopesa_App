from django.test import TestCase
import unittest
from django.test import Client
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from . import views
from .models import *
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.validators import FileExtensionValidator
from django.core.validators import validate_image_file_extension
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
#------------------------- END IMPORT FILES--------------------------------------

#############################################################################
# BASIC TESTS
#
#   Filename = principal:tests.py
#   Description:
#       - Testing for application " Principal"
#   Author : Arturo Borbolla
#   Role : Site Administrator
#   Last date of tests : 24/11/2018
#
#   Comments:
#       - Tests ran ok
#
#############################################################################



# NAVIGATION TESTS

class Navigation(TestCase):
    def setUp(self):
        self.client = Client()

    def test_navigateProperties(self):
        response = self.client.get('/properties/')
        self.assertEqual(response.status_code, 200)

    def test_navigateHome(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_navigateAbout(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_navigateContact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_navigateProperties(self):
        response = self.client.get('/properties/')
        self.assertEqual(response.status_code, 200)
#------------------------- END NAVIGATION TESTS --------------------------------------
#BASIC URL TEST
    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
#------------------------- END BASIC URL  TESTS --------------------------------------
#BASIC TEMPLATE TEST
    def test_view_uses_correct_templateHome(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gopesa_app/index.html')
#------------------------- END TEMPLATE RENDERING TESTS --------------------------------------
#CORRECT HTML TEST
    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'INICIO')
#------------------------- END CORRECT HTML TESTS --------------------------------------

#INCORRECT HTML TEST
    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')
#------------------------- END INCORRECT HTML TESTS --------------------------------------








# ADMIN TEST FUNCTIONALITIES