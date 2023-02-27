from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class stats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stats")
    score = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.score} {self.time}"
