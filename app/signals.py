from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Task, TaskHistory

@receiver(post_save, sender=Task)
def create_task_history(sender, instance, created, **kwargs):
    if not created:
        previous_status = Task.objects.get(pk=instance.pk).status
        if instance.status != previous_status:
            TaskHistory.objects.create(task=instance, previous_status=previous_status, new_status=instance.status)
