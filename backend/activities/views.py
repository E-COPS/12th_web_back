from rest_framework import viewsets
from .serializer import NewsSerializer
from .models import News

class NewsWiewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer