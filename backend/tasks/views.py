from django.shortcuts import render
from django.http import JsonResponse
from .models import Task

# Create your views here.

def task_list(request):
    tasks = list(Task.objects.values())
    return JsonResponse(tasks, safe=False)