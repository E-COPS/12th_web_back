from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChallengerViewSet

router = DefaultRouter()
router.register('', ChallengerViewSet)

urlpatterns = [
   path('', include(router.urls))
]