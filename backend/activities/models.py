from django.db import models


class News(models.Model):
    year = models.CharField(max_length=3, null=True, blank=False)#필수 데이터 
    type = models.CharField(max_length=40, null=True, blank=False)
    img = models.ImageField(upload_to='static/activities', null=True, blank=True)
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=30, default='')
    activity_description = models.TextField(null=True, blank=True)
    link = models.URLField(default='https://e-cops.tistory.com/', null=True, blank=True)
    git_link = models.URLField(null=True, blank=True)
    insta_link = models.URLField(default = 'https://www.instagram.com/ecops_ewha/')

    def __str__(self):
        return self.title