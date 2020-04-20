from django.db import models
import uuid
from devices.models import Device

# Create your models here.


class Task(models.Model):
    unique_task_id = models.UUIDField(
        default=uuid.uuid4(), editable=False, unique=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    task_todo = models.TextField(default="off")
    task_status = models.TextField(default="incomplete")
