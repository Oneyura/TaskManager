from django.contrib.auth.models import AbstractUser
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Task(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["status", "-date"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


class User(AbstractUser):
    pass
