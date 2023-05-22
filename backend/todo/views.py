from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.http import Http404
from . import serializers
from . import models


# Create your views here.


class TodoList(APIView):


    def get(self, request):
        todos = models.Todo.objects.all()
        serializer = serializers.TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    


class TodoDetail(APIView):


    def get_object(self, pk):
        try:
            return models.Todo.objects.get(pk=pk)
        except models.Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = serializers.TodoSerializer(todo)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        todo = self.get_object(pk)
        serializer = serializers.TodoSerializer(todo, data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        