from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('news', views.NewsViewSet)

app_name = 'news'

urlpatterns = [
    path('', include(router.urls)),
]