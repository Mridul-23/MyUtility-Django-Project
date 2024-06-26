from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NOTES(models.Model):

    title = models.CharField(max_length=52)
    content = models.TextField()
    user  = models.ForeignKey(User, on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)