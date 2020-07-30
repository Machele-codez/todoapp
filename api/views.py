from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import mixins

from .serializers import TaskSerializer
from .models import Task

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
  serializer_class = TaskSerializer
  queryset = Task.objects.all()