from django.http import JsonResponse


def home(request):
    hello = {
        "serverStatus": "ok",

    }
    return JsonResponse(hello)
