from django.db import models
from django.contrib.auth.models import User


class Stats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stats")
    score = models.IntegerField(default=0)
    time_spent = models.TimeField(default="00:00:00")
    data_history = models.TextField(default="")

    def __str__(self):
        return f"{self.user}"
