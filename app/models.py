from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class post(models.Model):
    postname = models.CharField(max_length=255,unique=True)
    shortdesc = models.TextField()
    description = models.TextField()
    date = models.DateField(default=True)
    def __str__(self):
        return self.postname


class likepost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    postname = models.ForeignKey(to=post,on_delete=models.PROTECT)


class commnetpost(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    postname = models.ForeignKey(to=post, on_delete=models.PROTECT)
    commnent = models.TextField()

    
    