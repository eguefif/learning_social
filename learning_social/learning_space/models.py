from django.db import models
from user.models import User


class LearningSpace(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
