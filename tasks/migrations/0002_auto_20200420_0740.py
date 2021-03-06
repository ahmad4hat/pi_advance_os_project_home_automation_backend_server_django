# Generated by Django 3.0.5 on 2020-04-20 07:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=models.TextField(default='incomplete'),
        ),
        migrations.AlterField(
            model_name='task',
            name='unique_task_id',
            field=models.UUIDField(default=uuid.UUID('c9b2f14a-bf65-42ce-9838-1070f14d8789'), editable=False, unique=True),
        ),
    ]
