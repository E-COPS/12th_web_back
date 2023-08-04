from django.db import models

class Members(models.Model):
    year = models.IntegerField()#필수 데이터 
    img = models.ImageField(upload_to='static/members/',blank=True) #이미지명은 학번 기준으로 하면 관리하기 좋을듯
    std_id=models.IntegerField(unique=True)
    name = models.CharField(max_length=100,unique=False)
    comment = models.TextField(max_length=12, blank=True,unique=False)#공백 가능
    insta_link = models.URLField(blank=True,unique=False)
    git_link = models.URLField(blank=True,unique=False)
    linkedin_link = models.URLField(blank=True,unique=False)
    tf=models.BooleanField(default=False, unique=False)


    def __str__(self):
        return self.name