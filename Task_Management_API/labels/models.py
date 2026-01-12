from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task

class Label(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='labels'
    )
    tasks = models.ManyToManyField(
        Task,
        related_name='labels',
        blank=True
    )

    def __str__(self):
        return self.name
