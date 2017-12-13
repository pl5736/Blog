from django.shortcuts import render
from MyBlog.models import User
from django.shortcuts import redirect
from django.conf import settings
import time
import random
import os

# Create your views here.


def login(request):
    if request.method == "POST":
        nameid = request.POST.get("userAccount")
        pswd = request.POST.get("userPass")
        try:
            user = User.objects.get(userAccount=nameid)
            if user.userPasswd != pswd:
                return redirect('/login/')
        except User.DoesNotExist as e:
            return redirect('/login/')

        # 登陆成功
        token = time.time() + random.randrange(1, 100000)
        user.userToken = str(token)
        user.save()
        request.session["username"] = user.userName
        request.session["userimg"] = user.userImg
        request.session["token"] = user.userToken
        return redirect('/')
    else:
        return render(request, 'temp/login.html')


def register(request):
    if request.method == "POST":
        userAccount = request.POST.get("userAccount")
        userPasswd = request.POST.get("userPass")
        userName = request.POST.get("userName")
        userPhone = request.POST.get("userPhone")
        userEmail = request.POST.get("userEmail")
        is_delete = 0
        confirmed = 0
        token = time.time() + random.randrange(1, 100000)
        userToken = str(token)
        f = request.FILES["userImg"]
        userImg_last = str(f).split('.')[-1]
        userImg = os.path.join(userAccount + '.' + userImg_last)
        absImg = os.path.join(settings.MDEIA_ROOT, userAccount)
        with open(absImg, "wb") as fp:
            for data in f.chunks():
                fp.write(data)

        user = User.createuser(userAccount, userPasswd, userName, userPhone,
                               userEmail, userImg, userToken, is_delete,
                               confirmed)
        user.save()

        request.session["username"] = userName
        request.session["userimg"] = userImg
        request.session["token"] = userToken

        return redirect('/')
    else:
        return render(request, 'temp/register.html')


def logout(request):
    request.session.clear()
    username = '未登录'
    context = {'username': username}
    return render(request, 'temp/index.html', context)


def home(request):
    if 'username' in request.session:
        username = request.session['username']
        if 'userimg' in request.session:
            img = request.session['userimg']
            img = '/static/mdeia/%s' % img
            context = {'username': username, 'img': img}
        else:
            pass
    else:
        username = '未登录'
        context = {'username': username}
    return render(request, 'temp/index.html', context)


def about(request):
    if 'username' in request.session:
        username = request.session['username']
        if 'userimg' in request.session:
            img = request.session['userimg']
            img = '/static/mdeia/%s' % img
            context = {'username': username, 'img': img}
        else:
            pass
    else:
        username = '未登录'
        context = {'username': username}
    return render(request, 'temp/about.html', context)


def gbook(request):
    if 'username' in request.session:
        username = request.session['username']
        if 'userimg' in request.session:
            img = request.session['userimg']
            img = '/static/mdeia/%s' % img
            context = {'username': username, 'img': img}
        else:
            pass
    else:
        username = '未登录'
        context = {'username': username}
    return render(request, 'temp/gbook.html', context)


def learn(request):
    if 'username' in request.session:
        username = request.session['username']
        if 'userimg' in request.session:
            img = request.session['userimg']
            img = '/static/mdeia/%s' % img
            context = {'username': username, 'img': img}
        else:
            pass
    else:
        username = '未登录'
        context = {'username': username}
    return render(request, 'temp/learn.html', context)


def manshenghuo(request):
    if 'username' in request.session:
        username = request.session['username']
        if 'userimg' in request.session:
            img = request.session['userimg']
            img = '/static/mdeia/%s' % img
            context = {'username': username, 'img': img}
        else:
            pass
    else:
        username = '未登录'
        context = {'username': username}
    return render(request, 'temp/manshenghuo.html', context)


def mbfx(request):
    if 'username' in request.session:
        username = request.session['username']
        if 'userimg' in request.session:
            img = request.session['userimg']
            img = '/static/mdeia/%s' % img
            context = {'username': username, 'img': img}
        else:
            pass
    else:
        username = '未登录'
        context = {'username': username}
    return render(request, 'temp/mbfx.html', context)
