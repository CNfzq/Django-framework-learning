'''展示页面的文件，返回需要展示的内容，路径在urls.py设置'''
from django.http import HttpResponse       #HttpResponse是一个响应类，返回内容给服务器

# 定义一个视图函数,用来处理请求的
# 括号里面的参数是用户发来的所有的请求，用户访问网站，发送一个请求，服务器后台接收，所以要在视图函数里面传入request请求
def hello(request):
    # x=1+'1'     #这个是自己写的异常，用于中间件类MyException来捕获异常，见mymiddleware.py文件
    return HttpResponse('你好')                 #HttpResponse相当于self.write(),把响应内容返回到浏览器界面

def hello_fzq(request):
    return HttpResponse('hello fzq???')

def hello_taka(request,name,age):
    return HttpResponse('hello %s,今年%s岁???'%(name,age))

def re_path_test(request):
    return HttpResponse('测试re_path')
