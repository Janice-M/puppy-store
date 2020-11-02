from django.test import TestCase
from . models import Puppy

''' test for puppy model'''

class PuppyTest(TestCase):
    
    def setUp(self):
        Puppy.objects.create(
            name = 'Frigg' , age = 4 , breed = 'Bull ' ,color = 'Black'
        )
        Puppy.objects.create (
            name = 'Thor' , age = 2 , breed = 'Chihuahua', color = 'brown'
        )
        
    def test_puppy_breed (self):
        puppy_frigg = Puppy.objects.get (name = 'Frigg')
        puppy_thor = Puppy.objects.get(name = 'Thor')
        
        self.assertEqual (
            puppy_frigg.get_breed(), "Frigg belongs to Bull breed ."
        )
        self.assertEqual(
            puppy_thor.get_breed(),  "Thor belongs to Chihuahua breed"
        )