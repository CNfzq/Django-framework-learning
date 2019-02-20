from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
'''
1.HttpRequest对象：
    视图函数接受到的request到底是个什么对象呢?
    服务器接收到http协议的请求后，会根据报文创建HttpRequest对象视图函数的第一个参数是HttpRequest对象在django.http模块中定义了HttpRequest对象的API
    属性：
        path:一个字符串，表示请求的页面的完整路径，不包含域名
        method:一个字符串，表示请求使用的HTTP方法，常用的值包括：GET，POST
        encoding:一个字符串，表示提交的数据的编码方式，如果为None则表示使用浏览器的默认设置，一般为utf_8
                 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值
        GET：一个类似于字典的对象，包含get请求方式的所有参数
        POST：一个类似于字典的对象，包含post请求方式的所有参数
        FILES：一个类似于字典的对象，包含所有的上传的文件
        COOKIES:一个标准的python字典，包含所有的cookie,键和值都为字符串
        session:一个既可读又可写的类似于字典的对象，表示当前的会话，只有当django启用会话的支持时才可用，详细内容见‘状态保持’ 
    方法：
        is_ajax:如果请求是通过XMLHttpRequest发起的，则返回True
'''

'''
form标签中的GET和POST:
    在HTML中,form表单的作用是收集标签中的内容,<form>...</form> 中间可以由访问者添加类似于文本,选择,或者一些控制模块等等.然后这些内容将会被送到服务端。

    一个表单必须指定两样东西：
    1. form的method参数用于设置表单的提交方式,默认使用POST.
    2. action用于设置表单的提交url,如果不写或者保持空字符串,那么将使用当前的URL.

request中GET和POST对象的属性:
        GET属性:
            - QueryDict类型的对象
            - 包含get请求方式的所有参数
            - 与url请求地址中的参数对应，位于?后面
            - 参数的格式是键值对，如key1=value1
            - 多个参数之间，使用&连接，如key1=value1&key2=value2
        POST属性:
            - QueryDict类型的对象
            - 包含post请求方式的所有参数
            - 与form表单中的控件对应
            - 表单中控件要有name属性，则name属性的值为键，value属性的值为值，构成键值对提交
            - 对于checkbox控件，name属性一样为一组，当控件被选中后会被提交，存在一键多值的情况.


GET和POST请求方式总结:
    1. GET:GET如其名，是从服务器获取数据，不会更改服务器的状态和数据，在URL中携带参数发送给服务器。
    2. POST则是将一定量的数据发送给服务器，一般会更改服务器的数据。
    3. POST方法的参数不能在URL当中看到,他是通过body参数传递给服务器的,所以相对GET方法直接能在URL当中看到传递的参数,显得更加安全一些.
        当然,也不能简单的判定POST方法比GET方法更安全,要使网站保持安全,需要做更多的安全处理.
'''
# POST请求,<form></form>表单的method默认是post
def post_test(request):
    if request.method=='GET':
        print(request.GET)        #返回的是一个字典类型（QueryDict），可用字典里的操作方法
        return render(request,'get_post.html')
    elif request.method=='POST':
        print(request.POST)       #返回的是一个字典类型（QueryDict），可用字典里的操作方法
        title=request.POST.get('title')
        content=request.POST.get('content')
        # 1.post的提交方式不会在url中显示参数
        # 2.可以通过request.POST.get方式来获取提交的数据
        print(title,content)
        return HttpResponse('post请求')

# GET请求,如果<form></form>表单的method是get
def get_test(request):
    print(request.path)
    print(request.method)
    print(request.GET)        ##返回的是一个字典类型（QueryDict），可用字典里的操作方法
    title = request.GET.get('title')
    content = request.GET.get('content')
    # 1.get提交的参数会在url中显示.
    # 2.可以通过request.GET.get的方法来获取提交的参数.
    print(title, content)
    # 假设<form></form>表单里的多选框有相同的name,不同的value,用request.GET/POST.get()方法只能获取value值的最后一个值
    # 想要获取全部的value值,QueryDict对象提供了一个getlist()方法
    title_list=request.GET.getlist('title')
    print(title_list)
    '''
        一键多值的getlist方法:
            request对象的属性GET、POST都是QueryDict类型的对象
            与python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况

                - 方法get()：
                根据键获取值,只能获取键的一个值
                如果一个键同时拥有多个值，获取最后一值
                - 方法getlist()：
                根据键获取值将键的值以列表返回
                可以获取一个键的多个值
    '''
    return render(request, 'get_post.html')





'''
    文件上传：
        Django在处理文件上传的时候,文件数据被保存在了request.FILES
        FILES中的每个键为<input type="file" name="" />中的name
    设置文件的存储路径：
        1.在项目根目录下static中创建media文件夹
        2.图片上传后，会被保存到“/static/media/文件”
        3.打开settings.py文件，增加media_root项：
            MEDIA_ROOT=os.path.join(BASE_DIR,'static/media')

'''
import os
from django_f.settings import MEDIA_ROOT
def upload_file(request):
    if request.method=='POST':
        print(request.FILES)      #返回的是一个字典类型，<MultiValueDict: {'file': [<InMemoryUploadedFile: 00.jpg (image/jpeg)>]}>
        rs=request.FILES.get('file')
        print(rs)    #打印的是文件名.扩展名，但是返回的是一条数据（包含文件名，文件数据等等）
        print(rs.name)   #打印的是文件名.扩展名，但就是文件名.扩展名
        file_path=os.path.join(MEDIA_ROOT,rs.name)
        with open(file_path,'wb') as f:
            for content in rs.chunks():       #chunks()方法指读取文件
                f.write(content)
    return render(request,'upload_files.html')




'''
    HttpResponse对象：
        属性：
            content:表示返回的内容，字符串类型
            charset:表示response采用的编码字符集，字符串类型
            status_code:响应的HTTP响应状态码
            content-type:指定输出的MIME类型
        方法：
            init:使用页内容实例化HttpResponse对象
            write(content):以文件的方式写
            flush():以文件的方式输出缓冲区
            set_cookie(key,value='',max_age=None,expires=None):设置cookie:
                        key,value都是字符串类型
                        max_age:是一个整型，表示在指定秒数后过期
                        expires:是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期，注意datetime和timedelta值只有在使用PickleSerializer时才可序列化
                        max_age和expires二选一
                        如果不指定过期时间，则关闭浏览器就失效
                        delete_cookie(key):删除指定的key的cookie,如果key不存在则什么也不发生
    HttpResponse的子类:
                    返回数据的响应函数有:
                            HttpResponse()   返回简单的字符串对象
                            render()   渲染模板
                            redirect()  重定向
                            JsonResponse()  返回json数据：
                                    - 帮助用户创建JSON编码的响应
                                    - 参数data是字典对象
                                    - JsonResponse的默认Content-Type为application/json
'''
def response_test(request):
    res=HttpResponse('这是返回的内容content')
    print(res)
    print(res.content)          #属性
    print(res.charset)          #属性
    print(res.status_code)      #属性
    # print(res.content-type)
    return res
# 返回的数据是json数据
from django.http import JsonResponse
def response_test2(request):
    json=JsonResponse({'fzq':21})
    print(json)    #返回的是<JsonResponse status_code=200, "application/json">
    return json



'''
    HTTP协议：
        HTTP（超文本传输协议）是一个应用层协议，由请求和响应构成，是一个标准的客户端服务器模型。HTTP是一个无状态的协议。
    无状态：不会记住客户端是谁访问，客户端再次访问服务器，服务器还是不知道是你再访问的
    Cookie:HTTP是一种无状态的协议，用于记录用户的状态
'''
# 一个项目只能对应一个cookie，cookie的作用域：整个项目都是同一个cookie
# 设置cookie
import datetime
def set_cookie(request):
    print(request.COOKIES)   #请求里面的cookie
    response=HttpResponse('cookie测试')   #响应里面先设置cookie，再发送到客户端保存
    response.set_cookie('name','fzq')  #默认浏览器关闭过期，set_cookie(名字，内容，约束)
    # response.set_cookie('name', 'fzq',max_age=60,expires=datetime.datetime(2018,11,25))  #自己设置过期时间，max_age单位是秒,指定天数可用datetime模块
    return response

#获取cookie
def get_cookie(request):
    cookie=request.COOKIES
    print(cookie)
    return HttpResponse('拿到cookie')

# 删除cookie
def delete_cookie(request):
    rs=HttpResponse('删除cookie')
    print(rs)
    rs.delete_cookie('name')
    return rs
'''
注意:设置cookie值以及删除cookie值都是response对象的操作,而获取cookie是从requeset相应中获得的.
'''



'''浏览器存储cookie的方式不太安全,那有没有更好些的来存储登入状态的方式呢???

    见cookie_session APP
'''
