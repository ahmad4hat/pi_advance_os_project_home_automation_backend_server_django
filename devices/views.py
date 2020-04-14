from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from . import models
import json

# Create your views here.


def input_data_error_finder_helper(received_json_data):
    errors = {}
    if(not ('name' in received_json_data) or received_json_data["name"] == ""):
        errors["name"] = "name is  empty or null"
    if(not ('description' in received_json_data) or received_json_data["description"] == ""):
        errors["description"] = "description is  empty or null"
    if(not ('type' in received_json_data) or received_json_data["type"] == ""):
        errors["type"] = "type is  empty or null"
    return errors


def all_devices(request):

    if(request.method == "POST"):
        value = {"post": True}
        print(request.body)
        received_json_data = json.loads(request.body)
        errors = input_data_error_finder_helper(received_json_data)
        if(len(errors) != 0):
            print(errors)
            return JsonResponse(errors, status=400)
        newDevice = models.Device()
        newDevice.name = received_json_data['name']
        newDevice.description = received_json_data["description"]
        newDevice.type = received_json_data["type"]
        newDevice.save()

        return JsonResponse(received_json_data)

    devices = serialize('json', models.Device.objects.all())
    device_decoded = json.loads(devices)

    reached_view = {"whatsGoingOn": "whatever"}
    return JsonResponse(device_decoded, safe=False)
