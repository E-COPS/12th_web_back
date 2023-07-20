from django.db import models
class News(models.Model):
    title = models.CharField(max_length=70)
    author = models.TextField(default='')
    year = models.TextField(default='')
    link = models.TextField(default = 'http://127.0.0.1:8000/')
    img = models.TextField(default = '')