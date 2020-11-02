from django.db import models

class Puppy(models.model):
    '''
    THIS CLASS HOLDA OUR PUP ATTRTIBUTES
    '''
    name = models.CharField(max_length = 255)
    age = models.IntegerField()
    breed = models.CharField(max_length = 255)
    color= models.CharField(max_length =255)
    created_at =models.DateTimeField(auto_now_add = True)
    updated_at = modesls.DateTimeField(auto_now = True)

    def get_breed(self):
        return self.name + 'belongs to' + self.breed + 'breed'