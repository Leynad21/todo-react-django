from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from . import serializers
from . import models

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer