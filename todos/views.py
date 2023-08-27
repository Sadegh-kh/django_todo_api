from django.shortcuts import render
from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializers

# Create your views here.


class ListTodoApi(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class DetailTodoApi(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
