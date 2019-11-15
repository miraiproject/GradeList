from django.db import models
from django.contrib.auth.models import User

from statistics import mean

# Create your models here.
        
class Grades(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    subject = models.CharField(max_length=50, null=False)
    english = models.PositiveIntegerField(default=0)
    math = models.PositiveIntegerField(default=0)
    japanese = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    gpa = models.PositiveIntegerField(default=0)

    def calculate_total(self):
        self.total = self.english + self.math + self.japanese
        
    def calculate_gpa(self):
        score = [self.english, self.math, self.japanese]
        gp = []
        for i in range(3):
            if score[i] >= 96:
                gp.append(4.3)
            elif score[i] >= 85:
                gp.append(4.0)
            elif score[i] >= 75:
                gp.append(3.0)
            elif score[i] >= 65:
                gp.append(2.0)
            elif score[i] >= 60:
                gp.append(1.0)
            else:
                gp.append(0.0)
        self.gpa = mean(gp)

    def __str__(self):
        return self.user.username
