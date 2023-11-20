from django.db import models


class UserRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class CreditEvaluationModel(models.Model):
    home_ownership = models.CharField(max_length=20)
    annual_inc = models.FloatField()
    loan_amnt = models.FloatField()
    emp_length = models.CharField(max_length=20)
    prediction = models.IntegerField()  # 1 for approved, 0 for rejected

from django.contrib.auth.models import User
