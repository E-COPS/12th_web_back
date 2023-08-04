from .models import Beginner
from .serializer import BeginnerSerializer
from rest_framework import viewsets

# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class BeginnerViewSet(viewsets.ModelViewSet):
    queryset = Beginner.objects.all()
    serializer_class = BeginnerSerializer
