from django.db import models
from django.conf import settings

# Create your models here.

class Challenger(models.Model):
    year = models.CharField(max_length=3, null=True, blank=False)#필수 데이터 
    track = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to='static/challenger', null=True, blank=True)
    program_name = models.CharField(max_length=50, null=True, blank=True)
    program_description = models.TextField(max_length=100, null=True, blank=True)
    insta_link = models.URLField(max_length=100, null=True, blank=True)
    git_link = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.program_name