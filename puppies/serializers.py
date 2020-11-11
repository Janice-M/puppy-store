from rest_framework import serializers
from .models import Puppy

class PuppySerializer (serializers.ModelSerializer):
    class Meta:
        model = Pup
        fields = ('name', 'age', 'breed', 'color', 'created_at', 'updated_at')