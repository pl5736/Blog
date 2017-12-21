from django.shortcuts import render
from MyBlog.models import User, Collection, Comment
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.conf import settings
from PIL import Image
import time
import random
import os

# Create your views here.


# 登录
def login(request):
    if request.method == "POST":
        nameid = request.POST.get("userAccount")
        pswd = request.POST.get("userPass")
        try:
            user = User.objects.get(userAccount=nameid)
            if user.userPasswd != pswd:
                return render(request, 'temp/login.html')
        except User.DoesNotExist as e:
            return render(request, 'temp/login.html')

        # 登陆成功
        token = time.time() + random.randrange(1, 100000)
        user.userToken = str(token)
        user.save()
        request.session["username"] = user.userName
        request.session["userimg"] = user.userImg
        request.session["token"] = user.userToken
        return render(request, 'temp/index.html')
    else:
        return render(request, 'temp/login.html')


# 注册
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
        absImg = os.path.join(settings.MDEIA_ROOT, userImg)
        userImg = os.path.join('/static/mdeia/' + userImg)

        img = Image.open(f)
        img = img.resize((40, 40), Image.ANTIALIAS)
        quality_val = 90
        img.save(absImg, quality=quality_val)

        user = User.createuser(userAccount, userPasswd, userName, userPhone,
                               userEmail, userImg, userToken, is_delete,
                               confirmed)
        user.save()

        request.session["username"] = userName
        request.session["userimg"] = userImg
        request.session["token"] = userToken

        return render(request, 'temp/index.html')
    else:
        return render(request, 'temp/register.html')


# 注册时检测账号是否可用
def checkAccount(request):
    account = request.GET.get('account')
    user = User.objects.filter(userAccount=account)
    if len(user) > 0:
        msg = '账号已存在'
        state = 201
    elif len(account) > 5 and len(account) < 13:
        msg = '账号可用'
        state = 200
    else:
        msg = '账号长度不正确'
        state = 201

    data = {'msg': msg, 'state': state}
    return JsonResponse(data)


# 注册时检测两次密码是否相同
def checkPassword(request):
    pwd = request.GET.get('pwd')
    pwdc = request.GET.get('pwdc')
    if len(pwd) > 6 and len(pwd) < 17 and len(pwdc) > 6 and len(pwdc) < 17:
        if pwd == pwdc:
            msg = '两次密码一致'
            state = 200
        else:
            msg = '两次密码不一致'
            state = 201
    else:
        msg = '密码长度不正确'
        state = 201

    data = {'msg': msg, 'state': state}
    return JsonResponse(data)


# 注册时检测用户名是否可用
def checkUsername(request):
    username = request.GET.get('username')
    user = User.objects.filter(userName=username)
    if len(user) > 0:
        msg = '用户名已存在'
        state = 201
    else:
        msg = '用户名可用'
        state = 200

    data = {'msg': msg, 'state': state}
    return JsonResponse(data)


# 登出
def logout(request):
    request.session.clear()
    return render(request, 'temp/index.html')


# 我的收藏
def collection(request):
    if 'username' in request.session:
        username = request.session['username']
        user = User.objects.get(userName=username)
        try:
            collection = Collection.objects.all().filter(user_id=user.userID)
            collect = []
            for c in collection:
                collect.append(('https://www.%s.com/' % c.path, c.collection))

            context = {'collection': collect}
            return render(request, 'temp/collection.html', context)
        except BaseException:
            return render(request, 'temp/collection.html')

    else:
        return render(request, 'temp/login.html')


# 添加收藏
def addCollection(request, collection, path):
    if 'username' in request.session:
        username = request.session['username']
        user = User.objects.get(userName=username)
        if not Collection.objects.filter(collection=collection
                                         ).filter(user_id=user.userID):
            collect = Collection()

            collect.user = user
            collect.collection = collection
            collect.path = path
            collect.save()
            return render(request, 'temp/index.html')
        else:
            return render(request, 'temp/index.html')
    else:
        return render(request, 'temp/login.html')


# 删除收藏
def delCollection(request, collection):
    if 'username' in request.session:
        username = request.session['username']
        user = User.objects.get(userName=username)
        collect = Collection.objects.all().filter(collection=collection).filter(
            user_id=user.userID)
        collect.delete()
        return HttpResponseRedirect('/collection/')


# 评论
def comment(request):
    if request.method == "POST":
        comm = request.POST.get('comment')
        if 'username' in request.session:
            username = request.session['username']
            user = User.objects.get(userName=username)
            comment = Comment()

            comment.user = user
            comment.comm = comm
            comment.save()
            return HttpResponseRedirect('/gbook/')
        else:
            return render(request, 'temp/login.html')


# 主页
def home(request):
    return render(request, 'temp/index.html')


# 关于我
def about(request):
    return render(request, 'temp/about.html')


# 留言
def gbook(request):
    try:
        comment = Comment.objects.all()
        comm = []
        for c in comment:
            user = User.objects.all().filter(userID=c.user_id)
            username = user[0].userName
            img = user[0].userImg
            comm.append((img, username, c.comm, c.date_publish))

        context = {'comment': comm}
        return render(request, 'temp/gbook.html', context)
    except BaseException:
        return render(request, 'temp/gbook.html')


# 学无止境
def learn(request):
    return render(request, 'temp/learn.html')


# 慢生活
def manshenghuo(request):
    return render(request, 'temp/manshenghuo.html')


# 模板分享
def mbfx(request):
    return render(request, 'temp/mbfx.html')
