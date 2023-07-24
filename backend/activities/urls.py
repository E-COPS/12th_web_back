from django.urls import include, path
from rest_framework import routers
from . import views
from activities.views import NewsViewSet

router = routers.DefaultRouter()
router.register('news', views.NewsViewSet)

app_name = 'news'

urlpatterns = [
    
]

urlpatterns += router.urls