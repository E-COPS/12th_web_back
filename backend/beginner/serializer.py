from rest_framework import serializers
from .models import Beginner

class BeginnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beginner
        fields = '__all__'
