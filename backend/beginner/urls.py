from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers
from .views import BeginnerViewSet

router = routers.DefaultRouter()
router.register('beginner', BeginnerViewSet)

# 세션 list 보여주기
beginner_list = BeginnerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# 세션 detail 보여주기, 수정, 삭제
beginner_detail = BeginnerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'

})

app_name = 'beginner'

urlpatterns = [
    path('', beginner_list),

    path('<int:pk>/', beginner_detail),

    path('', include(router.urls)),
    
]

# urlpatterns = format_suffix_patterns(urlpatterns)