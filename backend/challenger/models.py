from django.db import models
from django.conf import settings

# Create your models here.

class Challenger(models.Model):
    year = models.IntegerField(default=0, null=True, blank=True)
    img = models.ImageField(upload_to='challenger', blank=True, null=True)
    program_name = models.CharField(max_length=100, null=True, blank=True)
    program_description = models.TextField(null=True, blank=True)
    insta_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.year}기"