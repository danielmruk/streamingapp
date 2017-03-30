from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stream(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='stream')
    name = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='stream_logo/')

    def __str__(self):
        return self.name
