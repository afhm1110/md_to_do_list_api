from django.urls import path
from .views import ListList, ListDetail, TaskList, TaskDetail

urlpatterns = [
    path('lists/', ListList.as_view(), name='list-list'),
    path('lists/<int:pk>/', ListDetail.as_view(), name='list-detail'),
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>', TaskDetail.as_view(), name='task-detail'),
]