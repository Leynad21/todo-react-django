from django.urls import path, include
from .views import TodoList, TodoDetail
from rest_framework import routers


urlpatterns = [
    path('todo/', TodoList.as_view(), name='todo-list'),
    path('todo/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
]

