from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TODO(models.Model):
    status_choices = [
        ('C', 'COMPLETED'),
        ('P', 'PENDING'),
    ]
    priority_choices = [
        ('1', 'LOW'),
        ('2', 'MID'),
        ('3', 'HIGH'),
    ]
    title = models.CharField(max_length=52)
    status = models.CharField(max_length=2, choices=status_choices)
    user  = models.ForeignKey(User  , on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2 , choices=priority_choices)