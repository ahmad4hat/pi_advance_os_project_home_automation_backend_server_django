# Generated by Django 3.0.5 on 2020-04-20 07:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20200419_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='unique_device_id',
            field=models.UUIDField(default=uuid.UUID('a6c29ba9-d7f5-4498-b373-58bd410c1459'), editable=False, unique=True),
        ),
    ]
