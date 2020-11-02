from django.test import TestCase
from . models import Puppy

''' test for puppy model'''

class PuppyTest(TestCase):
    
    def setUp(self):
        Puppy.Objects.create(
            name = 'Frigg' , age = 4 , breed = 'Bull Dog' ,color = 'Black'
        )
        Puppy.Objects.create (
            name = 'Thor' , age = 2 , breed = 'chihuahua', coloe = 'brown'
        )
        
    def test_puppy_breed (self):
        puppy_frigg = Puppy.objects.get (name = 'Frigg')
        puppy_thor = Puppy.objects.get(name = 'Thor')
        
        self.assertEqual (
            puppy_frigg.get_breed(), "Frigg belongs to Bull Dog breed ."
        )
        self.assert