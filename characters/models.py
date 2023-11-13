from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    stats = models.JSONField(default=dict)

    def __str__(self):
        return self.name