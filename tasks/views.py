from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from . import models
import json

# Create your views here.


def all_task(request):
    return JsonResponse({"hello": 'hello'})


def queue_task(request):
    queue = [
        {
            "task_id": 1,
            "channel": 21,
            "task_todo": "on"
        },
        {
            "task_id": 2,
            "channel": 23,
            "task_todo": "off"
        }
    ]

    return JsonResponse(queue, safe=False)
