from django.test import TestCase
from . models import Puppy
from . import  __init__

class PuppyTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Puppy.objects.create(
            name='Frigg', age=3, breed='Bull Dog', color='Black')
        Puppy.objects.create(
            name='Thor', age=1, breed='Gradane', color='Brown')

    def test_puppy_breed(self):
        puppy_frigg = Puppy.objects.get(name='Frigg')
        puppy_thor = Puppy.objects.get(name='Thor')
        self.assertEqual(
            puppy_frigg.get_breed(), "Frigg belongs to Bull Dog breed.")
        self.assertEqual(
            puppy_thor.get_breed(), "Thor belongs to Gradane breed.")