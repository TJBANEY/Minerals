import unittest
from django.test import Client
import views
import models

class MineralTestCase(unittest.TestCase):
    c = Client()

    def setUp(self):
        models.Mineral.objects.all().delete()
        self.mineral1 = models.Mineral.objects.create(name='Unittestite')
        self.mineral2 = models.Mineral.objects.create(name='Randomite')
        self.mineral3 = models.Mineral.objects.create(name='Quartzite')
        self.mineral4 = models.Mineral.objects.create(name='Meteorite')
        self.minerals = models.Mineral.objects.all()

        self.mineral_length = len(self.minerals)

    def test_mineral_list(self):
        response = self.c.get('/')

        code = response.status_code
        context = response.context['all_minerals']
        context_length = len(context)

        self.assertTrue(code == 200)
        self.assertEqual(self.mineral_length, context_length)

    def test_mineral_detail(self):
        response = self.c.get('/mineral/3')

        code = response.status_code
        context = response.context['mineral']

        self.assertTrue(code == 200)
        self.assertEqual(self.mineral3, context)
