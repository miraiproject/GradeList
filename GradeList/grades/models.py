from django.db import models
from django.contrib.auth.models import User

from statistics import mean

# Create your models here.
        
class Grades(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    english = models.PositiveIntegerField(default=0)
    math = models.PositiveIntegerField(default=0)
    japanese = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    gpa = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username
