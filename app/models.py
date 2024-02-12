from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title


class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    previous_status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='previous_task_statuses')
    new_status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='new_task_statuses')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.title} - {self.status.name} - {self.assigned_to.username}"

    def clean(self):
        # Получаем текущий статус задачи
        current_status = self.status

        if self.pk:  
            previous_status = Task.objects.get(pk=self.pk).status
            if current_status.priority < previous_status.priority:
                raise ValidationError("Вы не можете изменить статус задачи на статус с более низким приоритетом.")

        super().clean()