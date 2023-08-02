from django.urls import path
from . import views

urlpatterns=[
    path('', views.apiOverview, name="api-overview"),
    path('list/', views.memberList, name="member-list"),
    path('detail/<int:year>/', views.memberDetail, name="member-detail"),
    path('create/', views.memberCreate, name='member-create'),
    path('update/<int:std_id>/', views.memberUpdate, name='member-update'),
    path('delete/<int:std_id>/', views.memberDelete, name='member-delete'),
]
