from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MembersViewSet

router = DefaultRouter()
router.register('', MembersViewSet)

urlpatterns=[
    # path('', views.apiOverview, name="api-overview"),
    # path('list/', views.memberList, name="member-list"),
    # path('detail/<int:year>/', views.memberDetail, name="member-detail"),
    # path('create/', views.memberCreate, name='member-create'),
    # path('update/<int:std_id>/', views.memberUpdate, name='member-update'),
    # path('delete/<int:std_id>/', views.memberDelete, name='member-delete'),
    path('', include(router.urls))
]
