from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Grades(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, null=False)
    score = models.PositiveIntegerField(max_digits=100)

    def calculate_gp(self):
        gp = 0
        if self.score >= 96:
            gp = 4.3
        elif self.score[i] >= 85:
            gp = 4.0
        elif self.score[i] >= 75:
            gp = 3.0
        elif self.score[i] >= 65:
            gp = 2.0
        elif self.score[i] >= 60:
            gp = 1.0
        else:
            gp = 0.0
