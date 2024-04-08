from django.db import models

class Talk(models.Model):
  topic = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  Talk = models.CharField(max_length=1000)
  posted_date = models.DateTimeField(auto_now_add=True)
  
def __str__(self):
    return f"{self.topic}"

from django.db import models
from django.utils import timezone

class Photo(models.Model):
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    upload_date = models.DateField(default=timezone.now)