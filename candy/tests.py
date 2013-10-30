"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from candy.candyownmodels import CandyOwnModels


class CandyCrazyTest(TestCase):
    def test_basic_flavour(self):
        """
        Tests that 5 + 1 always equals 6.
        """
        c = CandyOwnModels()
        six = c.no_model_here_but_an_int()
        self.assertEqual(5 + 1, six)

    def test_awesome_flavour(self):
        """
        Tests that 'chocolate' + '&' + 'honey' always equals 'chocolate&honey'.
        """
        c = CandyOwnModels()
        chocolate = c.no_model_here_but_an_string()
        self.assertEqual(chocolate + '&' + 'honey', 'chocolate&honey')

    def test_horrible_flavour(self):
        """
        Tests that 'IceKing' is a fake man.
        """
        self.assertNotEqual('IceKing', 'CoolestGuyInTheWorld')
