from rest_framework import serializers
from .models import Members

class MembersSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Members
        fields = '__all__'