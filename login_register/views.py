from django.shortcuts import render,redirect,reverse
from .forms import Login,Register
from .models import UserModel
from django.contrib.auth.hashers import make_password,check_password   #导入加密的方法，make_password：设置密码的时候（注册时用）check_password：检查密码的时候（登录时用）
from django.http import HttpResponse
from django.contrib.auth.models import User,Group,Permission    #导入auth系统提供的模型类
from django.contrib.auth import authenticate,login,logout       #导入auth系统提供的方法，authenticate 验证登录login 记住用户的登录状态logout 退出登录

# Create your views here.
def log_reg_index(request):
    name = request.session.get('username','XXX')
    return render(request,'index_log_reg.html',context={'name':name})
def login_i(request):
    form=Login()
    if request.method=='GET':
        return render(request, 'log.html', context={'form':form})
    elif request.method=='POST':
        form2= Login(request.POST)
        if form2.is_valid():
            username = form2.cleaned_data.get('username')
            password = form2.cleaned_data.get('password')
            # 方法1：自定义的模型类UserModel验证用户登录
            # user=UserModel.objects.filter(username=username)

            # 方法2：auth系统提供验证登陆的方法authenticate（）
            user=authenticate(username=username,password=password)   #用户名和密码与数据库里的相匹配
            if user:  #判断数据库里面是否存在该用户
                ''' 方法1：使用session记住用户的状态'''
                # if check_password(password,user[0].password): #检查密码是否一致
                #     request.session['username']=username    #设置session
                #     return redirect(reverse('log_reg_index'))
                # else:
                #     return render(request,'log.html',context={'error':form2.errors})
                '''方法2：auth系统提供login()方法记住用户的登录状态'''
                login(request,user)
                return redirect(reverse('log_reg_index'))
            else:
                return redirect(reverse('reg'))

        else:
            return redirect(reverse('log_reg_index'))
def logout_o(request):
    # 方法1:session删除状态
    # request.session.flush()        #删除session,session表里面删除

    # 方法2：auth系统提供删除记录的状态方法logout()
    logout(request)
    return redirect(reverse('log_reg_index'))
def register(request):
    form1 = Register(request.POST)
    if request.method == 'GET':
        return render(request, 'reg.html', context={'form1': form1})
    elif request.method == 'POST':
        # POST提交的数据在模型类Register拿，而不是在前端页面拿
        if form1.is_valid():      #is_valid():判断数据是否合法，就是跟模型类Register定义的字段是否一致
            # 模型类Form提供了拿取数据的方法
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password')
            password_repeat = form1.cleaned_data.get('password_repeat')
            email= form1.cleaned_data.get('email')
            if password==password_repeat:
                # # 方法1：自定义的模型类数据库添加用户信息
                # password=make_password(password)
                # user=UserModel(username=username,password=password,email=email)
                # user.save()
                # 方法2：使用auth系统提供的方法create_user（） 创建用户，添加用户到auth系统提供的数据表（auth_user）里
                user=User.objects.create_user(username=username,password=password,email=email) #密码会自动在数据库里帮我们加密的

                # 方法1：使用session记住用户的状态，auth系统提供了一个方法用于 记住用户的登录状态login（）
                # request.session['username'] = username  # 设置session

                # 方法2：auth系统提供login()方法记住用户的登录状态
                login(request,user)
                return redirect(reverse('log_reg_index'))
            else:
                return HttpResponse('密码不一致，请重新输入密码！！！')
        else:
            return HttpResponse('数据不合法，请重新注册！！！')



'''
request到底是哪来的：
    request就是用户访问浏览器发来的请求，request里面本身就有user属性，也就是说django设置好了这个属性，不是自己设置的user,也不是自己在中间件设置的
    用了auth系统，就可以直接用request去调用这个属性了，不用自己再去写这个属性了，只要发来一个请求，就能用这个请求判断当前用户是谁
'''