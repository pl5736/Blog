from django.db import models

# Create your models here.


class User(models.Model):
    userID = models.IntegerField(primary_key=True)
    userAccount = models.CharField(max_length=20, unique=True)
    userPasswd = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    userPhone = models.CharField(max_length=20)
    userEmail = models.CharField(max_length=30)
    userImg = models.CharField(max_length=150)
    userToken = models.CharField(max_length=50)
    is_delete = models.BooleanField(default=0)
    confirmed = models.BooleanField(default=0)

    @classmethod
    def createuser(cls, account, passwd, name, phone, email, img, userToken,
                   is_delete, confirmed):
        u = cls(userAccount=account, userPasswd=passwd, userName=name,
                userPhone=phone, userEmail=email, userImg=img,
                userToken=userToken, is_delete=is_delete, confirmed=confirmed)
        return u
