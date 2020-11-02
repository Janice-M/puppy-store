from django.test import TestCase
from . models import Puppy

''' test for puppy model'''

class PuppyTest(TestCase):
    
    def setUp(self):
        Puppy.Objects.create(
            name = 'Frigg' , age = 4 , breed = 'Bull Dog' ,color = 'Black'
        )
        Pu