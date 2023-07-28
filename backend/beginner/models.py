from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Beginner(models.Model):
    year = models.IntegerField(max_length=3, null=True, blank=True)
    track = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to='static', null=True, blank=True)
    program_name = models.CharField(max_length=100, null=True, blank=True)
    program_description = models.CharField(max_length=100, null=True, blank=True)
    insta_link = models.CharField(max_length=100, null=True, blank=True)
