from django.shortcuts import render

# Create your views here.
'''1.模板路径配置及模板变量:
        模板路径配置：
            第一种方式：
                    在项目目录下新建一个模板目录(与其他子目录同级)，
                    然后在模板目录下新建各子APP的模板文件
            第二种方式：
                    在各子目录(子APP)里面新建一个模板目录(templates)，
                     然后在settings文件里面的INSTALLED_APPS=[]添加子APP即可
        模板变量：除了字符串还可以是其他的类型
            
'''
def index_03_01(request):
    # context可以传入的类型可以是字符串，数值，列表，元组，字典，集合，函数对象，类对象(一般先实例化后传入对象，在模板文件里用实例去点.方法)
    list=['语文','数学','英语']              #如果传入的是迭代对象，比如列表元组字典集合等等，需要取某个值，就必须使用 . (list.0)符号去取属性值
    tuple=('1号','2号','3号')
    dict={'a':'12','b':'34'}
    # 函数
    def function():
        return '传递函数类型的对象'
    # 类对象
    class fzq:
        def __init__(self,name,age):
            self.name=name
            self.age=age
        def memoth(self):
            return '传递类对象的类型'
    c=fzq('fff',18)    #类对象(一般先实例化后传入对象，在模板文件里用实例去点.方法)
    context={'name':'fzq',
             'age':18,
             'sex':'男',
             'list':list,
             'tuple':tuple,
             'dict':dict,
             'func':function(),  #函数
             'c':c}   #类对象
    return render(request, '03/03_index_01.html', context=context)      #context参数必须是字典类型的,模板文件里面的占位符必须是键，通过键取值

'''2.模板过滤器：
        作用: 对变量进行过滤。在真正渲染出来之前，过滤器会根据功能处理好变量，然后得出结果后再替换掉原来的变量展示出来。
        语法：{{  |  }} 管道符号进行链式调用
        具体操作见03_index_02.html

'''
from datetime import datetime
def index_03_02(request):
    context={'str':'a sdf gh jk l',
             'str1':'qwertty',
             'num':11,
             'num1':22,
             'list':[1,2,3],
             'list1':[4,5,6],
             'default':None,
             'now':datetime.now(),
             'html':'<h1>hello django???</h1>',
             'float':3.1415926,
             'str2':'obvcxzasd',
             'str3':'this is fzq'

             }
    return render(request, '03/03_index_02.html', context=context)

'''
3.静态文件的设置路径:
            1.STATIC_URL = '/static/'
            或者
            2.STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
  静态文件的引用：
            见 03_index_03.html         
'''
def static_files(request):
    return render(request,'03/03_index_03.html')