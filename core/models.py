from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class stats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stats")
    score = models.IntegerField(default=0)
    timeSpent = models.TimeField(default="00:00:00")
    dataHistory = models.TextField(default="")

    def __str__(self):
        return f"{self.user}"
