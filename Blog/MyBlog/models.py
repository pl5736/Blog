from django.db import models

# Create your models here.


class User(models.Model):
    userID = models.IntegerField(primary_key=True)
    userAccount = models.CharField(max_length=20, unique=True)
    userPasswd = models.CharField(max_length=20)
    userName = models.CharField(max_length=20, unique=True)
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


class Collection(models.Model):
    collectionID = models.IntegerField(primary_key=True)
    collection = models.CharField(max_length=150)
    path = models.CharField(max_length=100)

    user = models.ForeignKey(User)


class Comment(models.Model):
    commentID = models.IntegerField(primary_key=True)
    comm = models.TextField()
    date_publish = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User)
    pid = models.ForeignKey('self', blank=True, null=True)
