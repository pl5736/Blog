from django.shortcuts import render
from .forms.login import LoginForm
from MyBlog.models import User
from django.shortcuts import redirect
from django.conf import settings
import time
import random
import os

# Create your views here.


def login(request):
    if request.method == "POST":
        f = LoginForm(request.POST)
        if f.is_valid():
            nameid = f.cleaned_data["username"]
            pswd = f.cleaned_data["passwd"]
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
            request.session["token"] = user.userToken
            return redirect('/')
        else:
            return render(request, 'temp/index.html', {"title": "登陆", "form": f, "error": f.errors})
    else:
        f = LoginForm()
        return render(request, 'temp/login.html', {"title": "登陆", "form": f})


def register(request):
    if request.method == "POST":
        userAccount = request.POST.get("userAccount")
        userPasswd = request.POST.get("userPass")
        userName = request.POST.get("userName")
        userPhone = request.POST.get("userPhone")
        userAdderss = request.POST.get("userAdderss")
        userRank = 0
        token = time.time() + random.randrange(1, 100000)
        userToken = str(token)
        f = request.FILES["userImg"]
        userImg = os.path.join(settings.MDEIA_ROOT, userAccount + ".png")
        with open(userImg, "wb") as fp:
            for data in f.chunks():
                fp.write(data)

        user = User.createuser(userAccount, userPasswd, userName, userPhone, userAdderss, userImg, userRank, userToken)
        user.save()

        request.session["username"] = userName
        request.session["token"] = userToken

        return redirect('/')
    else:
        return render(request, 'temp/register.html', {"title": "注册"})


def home(request):
    return render(request, 'temp/index.html')


def about(request):
    return render(request, 'temp/about.html')


def gbook(request):
    return render(request, 'temp/gbook.html')


def learn(request):
    return render(request, 'temp/learn.html')


def manshenghuo(request):
    return render(request, 'temp/manshenghuo.html')


def mbfx(request):
    return render(request, 'temp/mbfx.html')
