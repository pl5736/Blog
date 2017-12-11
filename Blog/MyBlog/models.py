from django.db import models

# Create your models here.


class User(models.Model):
    userAccount = models.CharField(max_length=20, unique=True)
    userPasswd = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    userPhone = models.CharField(max_length=20)
    userAdderss = models.CharField(max_length=100)
    userImg = models.CharField(max_length=150)
    userRank = models.IntegerField()
    userToken = models.CharField(max_length=50)

    @classmethod
    def createuser(cls, account, passwd, name, phone, address, img, rank, token):
        u = cls(userAccount=account, userPasswd=passwd, userName=name, userPhone=phone, userAdderss=address, userImg=img, userRank=rank, userToken=token)
        return u
