from .models import Challenger
from rest_framework import serializers

class ChallengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenger
        fields = '__all__'