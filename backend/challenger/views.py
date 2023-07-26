from rest_framework import viewsets
from .models import Challenger
from .serializers import ChallengerSerializer

# Create your views here.

class ChallengerViewSet(viewsets.ModelViewSet):
    queryset = Challenger.objects.all()
    serializer_class = ChallengerSerializer