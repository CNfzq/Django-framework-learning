'''自定义过滤器和标签'''


'''
django.template.Library.filter()
1.Library.filter()方法需要两个参数：
	a. 过滤器的名称（一个字符串对象）
	b. 编译的函数 – 一个Python函数（不要把函数名写成字符串）
2.可以把register.filter()用作装饰器;
3.没有声明 name 参数，Django将使用函数名作为过滤器的名字。

'''
from django import template          #导入模板模块
# 该模块提供一个方法，用于注册
register=template.Library()              #register是固定写法，Library是一个类，用这个类生成一个对象，实例化register
# 用register对象注册，register也可以作为装饰器使用

'''方法2'''
@register.filter           #使用语法糖，作为装饰器使用
# 简单的定义一个函数,过滤器就是一个简单的函数，要用到过滤器就要把函数转换成我们需要的过滤器格式,还要注册
def my_lower(value):
    return value.lower()

# 自定义一个带参数的过滤器
@register.filter
def my_cut(value,arg):
    return  value.replace(arg,'')

'''方法1'''
register.filter(my_lower)      #调用filter()方法，把自定义的函数扔进去注册，装饰成过滤器


'''
自定义过滤器就是一个带有一个或两个参数的Python 函数：
- （输入的）变量的值 —— 不一定是字符串形式。
- 参数的值 —— 可以有一个初始值，或者完全不要这个参数。
'''


'''自定义标签：   
        简单标签
        包含标签
        
    简单标签django.template.Library.simple_tag()
    包含标签django.template.Library.inclusion_tag()
        tag()方法有两个参数：
            1. 模板标记的名称 - 字符串。 如果省略，将使用编译函数的名称。
            2. 编译的函数 – 一个Python函数（不要把函数名写成字符串）
            与过滤器注册一样，也可以将其用作装饰器。
'''
# 简单标签
import datetime
@register.simple_tag        #注册一下，做为装饰器
def current_time(format_string):   #把自己想要的时间格式像参数一样传进来
            return datetime.datetime.now().strftime(format_string) #返回的是自己传入时间格式的结果，调用strftime()格式化时间的方法，将现在的时间按照自己需要的格式输出

# context上下文传参数
@register.simple_tag(takes_context=True)
def current_time1(context):
    format_string=context.get('format_time')
    return datetime.datetime.now().strftime(format_string)

# 包含标签
# 1.不传参数的标签
@register.inclusion_tag('04/包含标签.html')
def show_result():
    name=['哈哈','呵呵','嘿嘿']
    return {'choice':name}

# 2.不固定变量，通过传递参数
@register.inclusion_tag('04/包含标签.html')
def show_result1(li):
    return {'choice':li}