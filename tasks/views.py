from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from . import models
from devices.models import Device
import json

# Create your views here.


def all_task(request):
    if(request.method == "POST"):
        received_json_data = json.loads(request.body)
        newTask = models.Task()
        newTask.task_todo = received_json_data["task_todo"]
        device = Device.objects.get(
            unique_device_id=received_json_data["device_id"])
        newTask.device = device
        newTask.task_status = "incomplete"
        newTask.save()
        return JsonResponse(received_json_data)

    tasks = serialize('json', models.Task.objects.all())
    task_decoded = json.loads(tasks)
    return JsonResponse(task_decoded, safe=False)


def queue_task(request):

    tasks = models.Task.objects.filter(task_status__contains='incomplete')
    queue = []

    for task in tasks:
        task_dict = {
            "task_id": task.unique_task_id,
            "channel": task.device.channel,
            "task_todo": task.task_todo
        }
        queue.append(task_dict)

    return JsonResponse(queue, safe=False)
