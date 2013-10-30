"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class CandyCrazyTest(TestCase):
    def test_basic_flavour(self):
        """
        Tests that 5 + 1 always equals 6.
        """
        self.assertEqual(5 + 1, 6)

    def test_awesome_flavour(self):
        """
        Tests that 'choclate' + '&' + 'honey' always equals 'chocolate&honey'.
        """
        self.assertEqual('chocolate' + '&' + 'honey', 'chocolate&honey')

    def text_horrible_flavour(self):
        """
        Tests that 'IceKing' is a fake man.
        """
        self.assertNotEqual('IceKing', 'CoolestGuyInTheWorld')
