from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import mixins

from .serializers import TaskSerializer
from .models import Task

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
  serializer_class = TaskSerializer
  queryset = Task.objects.all()

class TestView(generic.View):
  def get(self, request):
    queryset = Task.objects.all()
    serializer = TaskSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
    