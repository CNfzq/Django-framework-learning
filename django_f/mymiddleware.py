'''定义中间件'''
# 中间件
'''
    django中的中间件:
        django 中的中间件（middleware），在django中，中间件其实就是一个类，在请求到来和结束后，django会根据自己的规则在合适的时机执行中间件中相应的方法。
        在django项目的settings模块中，有一个 MIDDLEWARE_CLASSES 变量，其中每一个元素就是一个中间件.

    中间件的引入：
        Django中间件（Middleware）
        是一个轻量级、底层的“插件”系统，可以介入Django的请求和响应处理过程，修改Django的输入或输出.
        用户----（request）----->中间件----（request）----->urls-->视图
        用户<----（response）<-----中间件<----（response）-----urls<--视图
    中间件的结构:
        中间件中可以定义5个方法，分别是：
                process_request(self,request) :
                执行视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
                process_view(self, request, callback, callback_args, callback_kwargs):
                调用视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
                process_template_response(self,request,response):
                在视图刚好执行完毕之后被调用，在每个请求上调用，返回实现了render方法的响应对象
                process_exception(self, request, exception)
                当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象
                process_response(self, request, response)
                所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象
    中间的执行顺序:
        请求以自上而下的顺序通过所有的层，view函数处理之后，响应以自下而上的顺序通过所有的层，期间经过的每个中间件都会对请求或者响应进行处理。
    注册中间件:
        注册到settings.py中间件中去MIDDLEWARE = ['项目名.文件名.自定义中间件的类']
'''
# 自定义中间件的第一种例子：使用中间件提供的5个方法
from login_register.models import UserModel
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin   #导入中间件的类
class Middleware(MiddlewareMixin):                    #继承中间件类
    def process_request(self,request):
        print('这是执行视图之前被调用的操作，在每个请求上调用，返回None或HttpResponse对象')
        return None
    def process_view(self,request,callback,callback_args,callback_kwargs):
        print('调用视图之前被调用的操作，在每个请求上调用，返回None或HttpResponse对象')
        return None
    def process_template_response(self,request,response):
        print('在视图刚好执行完毕之后被调用，在每个请求上调用，返回实现了render方法的响应对象')
        return response
    # def process_exception(self, request, exception):
    #     print(' 当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象')
    #     return HttpResponse(exception)
    def process_response(self, request, response):
        print('所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象')
        return response
# 用process_exception()方法来写一个例子：项目里所有视图若出现了异常都会来这里处理并捕获
class MyException(MiddlewareMixin):
    def process_exception(self,request,exception):
        print('自定义的异常处理中间件')
        return HttpResponse(exception)

# 自定义中间件的第一种例子：创建一个UserMiddleware的类,是给request请求增加一个myuser的属性,以这一句为分界,分别在view之前执行和view之后执行
class UserMiddleware(MiddlewareMixin):
    def __init__(self,request):
        self.response=request
        super().__init__()
    def __call__(self,request):
        name = request.session.get('username','游客')
        user=UserModel.objects.filter(username=name).first()
        if user:
            setattr(request,'myuser',user.username)
        else:
            setattr(request,'myuser','未登录')
        #上面的是request到达时之前的
        # 下面是response到达用户浏览器之前执行的
        response=self.response(request)
        return response