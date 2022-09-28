from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    date = models.CharField(max_length=255)
    title = models.TextField()
    description = models.CharField(max_length=255)
    is_finished = models.BooleanField(default=False)