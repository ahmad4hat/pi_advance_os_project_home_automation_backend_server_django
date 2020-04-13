from django.db import models
import uuid

# Create your models here.


class Device(models.Model):
    unique_device_id = models.UUIDField(default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255)
    current_state = models.CharField(max_length=255, default="off")
    current_value = models.TextField(null=True)
