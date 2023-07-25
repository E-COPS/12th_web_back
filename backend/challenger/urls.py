from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('challenger/', views.ChallengerList.as_view()),
    path('challenger/<int:pk>/', views.ChallengerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)