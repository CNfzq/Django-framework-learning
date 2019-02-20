'''
    浏览器存储cookie的方式不太安全,那有没有更好些的来存储登入状态的方式呢???
    session是什么：
         session保存在服务器，cookie保存在客户端
        session是怎么回事：在session这里django提供了一张session表来存储用户的sessionID和用户的信息,把用户的信息存放在一张表里
        把用户的sessionID（唯一的字段）返回给客户端，客户端就把sessionID存放在cookie里面去，下次登录，就会匹配sessionID是否一致

    状态保持:
        1.http协议是无状态的：每次请求都是一次新的请求，不会记得之前通信的状态
        2.客户端与服务器端的一次通信，就是一次会话实现状态保持的方式：在客户端或服务器端存储与会话有关的数据
        3.存储方式包括cookie、session，会话一般指session对象
        4. 使用cookie，所有数据存储在客户端，注意不要存储敏感信息
        5.使用sesison方式，所有数据存储在服务器端，在客户端cookie中存储session_id
        6.状态保持的目的是在一段时间内跟踪请求者的状态，可以实现跨页面访问当前请求者的数据
        - 注意：不同的请求者之间不会共享这个数据，与请求者一一对应
    如何启用session:
        1.在settings.py文件中:
            注册必须有：INSTALLED_APPS = ['django.contrib.sessions']（默认启用的）
            中间件必须有：MIDDLEWARE = ['django.contrib.sessions.middleware.SessionMiddleware']（默认启用的）
            数据库必须有django_session表：
                注: 使用session之前需要先执行makemigrations,migrate的模型映射文件命令,在数据库中有生成django_session的表格.
    如何使用session：
         启用会话后，每个HttpRequest对象将具有一个session属性，它是一个类字典对象
        - get(key, default=None)：根据键获取会话的值
        - clear()：清除所有会话
        - flush()：删除当前的会话数据并删除会话的Cookie
        - del request.session['member_id']-：删除
    会话过期时间:
        - set_expiry(value)：设置会话的超时时间
            - 如果没有指定，则两个星期后过期
            - 如果value是一个整数，会话将在values秒没有活动后过期
            - 如果value是一个imedelta对象，会话将在当前时间加上这个指定的日期/时间过期
            - 如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期
            - 如果value为None，那么会话永不过期

        也可以在setting文件中的配置会话过期时间：
            # 是否关闭浏览器使得Session过期，默认是False
            SESSION_EXPIRE_AT_BROWSER_CLOSE=False
            # 是否每次请求都保存Session,默认修改之后才保存
            SESSION_SAVE_EVERY_REQUEST=False
            # Session的cookie失效日期，默认是2周
            SESSION_COOKIE_AGE=1209600
            见setting.py


'''
'''
    以下是用户登录状态例子:
        1.一个既可读又可写的类似于字典的对象，表示当前的会话.
        2.在登录中使用request.session设置一个登录的信息.
        3.在主页面中获取设置的值,然后传给模板.
        4.使用request.session.flush()清除会话数据.
'''
from django.shortcuts import render,redirect,reverse
# Create your views here.
def index(request):
    # name='fzq'
    name=request.session.get('username','游客')    #拿到session
    return render(request,'index.html',context={'name':name})
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        request.session['username']=username    #设置session
        return redirect(reverse('index'))
def logout(request):
    request.session.flush()        #删除session,session表里面删除
    return redirect(reverse('index'))



