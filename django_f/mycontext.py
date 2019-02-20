'''
    上下文处理器是个什么东西呢?:
        上下文处理器的引入:
            在模板中想要使用的变量是从视图函数中的context这个上下文的参数中传递进来的,每个视图函数需要什么参数就传什么参数.
            上下文处理器就是创建模板变量.
            在settings.py中(TEMPLATES = ['OPTIONS': {'context_processors':[上下文处理器]}])，包含了当前使用的上下文处理器。他的作用是可以给每一个模板都提供相同的变量
        注册上下文处理器:
            将自定义的上下文处理器注册到settings.py中间件中：
                在TEMPLATES->OPTIONS->context_processors中加项目名.文件名.自定义的上下文处理器的函数
'''
from login_register.models import UserModel
def myuser(request):
    name=request.session.get('username','游客')
    user = UserModel.objects.filter(username=name).first()
    if user:
        return {'myuser':user.username}
    else:
        return {}



'''
中间件和上下文的总结:
    我们刚才分别用中间件和上下文完成了跟登录用户有关的例子, 最后的结果都是能在页面上显示用户的用户名了.
    中间件是在用户请求到响应的过程中去加入一些额外的逻辑功能,
    例子中给request增加了一个myuser的属性.
    上下文是给所有的模板增加变量
    例子中给模板增加了一个myuser的变量.


'''