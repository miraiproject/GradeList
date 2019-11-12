from django.db import models
from django.contrib.auth.models import User

from statistics import mean

# Create your models here.
        
class Grades(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    subject = models.CharField(max_length=50, null=False)
    english = models.PositiveIntegerField()
    math = models.PositiveIntegerField()
    japanese = models.PositiveIntegerField()

    def calculate_total(self, english, math, japanese):
        total = english + math + japanese
        total.save()
        
    def calculate_gpa(self, english, math, japanese):
        self.score = [english, math, japanese]
        gp = []
        for i in range(3):
            if self.score[i] >= 96:
                gp.append(4.3)
            elif self.score[i] >= 85:
                gp.append(4.0)
            elif self.score[i] >= 75:
                gp.append(3.0)
            elif self.score[i] >= 65:
                gp.append(2.0)
            elif self.score[i] >= 60:
                gp.append(1.0)
            else:
                gp.append(0.0)
        gpa = mean(gp)
        gpa.save()