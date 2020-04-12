from django.http import JsonResponse


def home(request):
    hello = {
        "myName": "whats",
        "wasx": 45
    }
    return JsonResponse(hello)
