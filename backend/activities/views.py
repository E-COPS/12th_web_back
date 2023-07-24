from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializer import NewsSerializer
from .models import News

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request):
        queryset = News.objects.all()
        print(queryset)
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)
