from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', csrf_exempt(views.all_task), name="all_task"),
    path('queue/', csrf_exempt(views.queue_task), name="task_queue"),



]
