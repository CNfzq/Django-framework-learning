from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

"""
'''数据库的相关操作一般在视图函数里写'''
from . import models   #导入模型文件，要使用里面的模型类（表）

# 添加数据
def add_user(request):
    '''方法1：通过模型类，往里面传参，这个参数就是字段名，模型类会接收相应字段的值'''
    # 先实例化类,通过对象去保存
    args=models.User(name='fzq',age=18)
    args.save()   #保存对象到数据库里面

    '''方法2：跟python里面类实例化一样的操作'''
    args1=models.User()   #实例化对象
    args1.name='辣椒'     #通过对象.属性
    args1.age=21
    args1.save()
    '''方法3：User类提供一个objects对象，这个对象里面包含了很多方法，与上面几种方法相比较，该方法不用save()的操作，会自动帮我们保存的'''
    models.User.objects.create(name='fzq',age=21)  #objects提供一个新建的方法create(),用来插入数据用的,但是，该方法不用再写save()方法保存了

    '''方法4：和方法3差不多，但是又有区别。方法3假如有相同的值，一样会添加进去，没有去重的功能
              方法4:如果存在了就不添加还会返回一个错误的页面，不存在就添加进去，有去的功能'''
    # models.User.objects.get_or_create(name='fzq',age=18)   #数据库里有重复的值会返回报错
    return HttpResponse('添加数据成功')

# 查询数据
def search_user(request):
    '''
    1.查找所有数据：
            all()和filter()方法返回的是QuerySet对象.
            get()方式返回的单个对象,如果符合条件的对象有多个,则get报错！
    '''
    data=models.User.objects.all()  #查到数据库里所有的数据，返回的是一个QuerySet对象类型，所有的数据都在这个对象里
    print(data)
    print(data[1])    #可用索引取值,也可以for循环遍历
    print(data[1].name)  #查字段的值
    print(data[2:5])     #也可以支持切片，不支持负索引取值

    '''2.查找某一条数据'''
    data1=models.User.objects.get(id=2)         #get()查询的值必须是唯一的值，id是唯一的
    print(data1)          #输出的是User<id=2,name=fzq,age=18>，这是模型类实例对象，拿到的是表里面的一条数据
    print(data1.name)
    print(data1.age)
    # data2 = models.User.objects.get(name='fzq')  #会报错，get()只能拿数据是唯一的值，不能够重复的值
    # print(data2)

    '''3.按照条件查询数据'''
    data3=models.User.objects.filter(name='fzq')             #把自己需要的筛选条件加进去，查询重复的数据不会报错
    print(data3)       #返回的是QuerySet对象，可以索引取值
    # QuerySet对象也提供了一些方法取值
    print(data3.first())   #获取第一条数据
    print(data3.last())    #获取最后一条数据
    return HttpResponse('查询数据成功')

'''
    数据库相关的接口（QuerySet API):
        1.从数据库中查询出来的结果一般是一个集合，这个集合叫做 QuerySet.
        2.QuerySet是可迭代对象.
        3.QuerySet支持切片, 不支持负索引.
        4.可以用list强行将QuerySet变成列表.

'''

# 删除数据
def delete_user(request):
    '''
        某个对象是否有某种方法,可以通过dir(obj)来进行查看.

    '''
    models.User.objects.filter(name='小付').delete()
    models.User.objects.get(name='小黄').delete()     #get()返回的是实例的对象（类的实例），也就是表里面的一条数据
    return HttpResponse('删除数据成功')

# 更新数据
def update_user(request):
    '''方法1：直接使用update()方法修改'''
    models.User.objects.filter(name='小黄').update(name='辣椒')
    '''方法2：get()方法查询返回的是模型类实例对象，拿到的是表里面的一条数据
                拿到的数据不能直接update(),只能通过实例.属性的方式去更新数据
    '''
    # 先查找到数据，再属性赋值修改
    result=models.User.objects.get(name='小李子')
    result.name='李子'
    result.save()        #切记：一定要保存
    return HttpResponse('更新数据成功')




'''把查询数据单独拿出来研究，常用的查询方法和查询条件'''
'''查询方法'''
# filter(**kwargs)方法：根据参数提供的提取条件，获取一个过滤后的QuerySet
data=models.User.objects.filter(name='fzq',age=18)    #多个条件用逗号（,）隔开即可

# exclude()方法：排除某个条件：排除 （name=辣椒） 的记录
data1=models.User.objects.exclude(name='辣椒')

# 获取一个记录对象（表里面的一条数据）
data2=models.User.objects.get(name='李子')
# 注意：get()返回的对象具有唯一性质，如果符合条件的对象有多个，则会报错

# order_by:对查询出来的数据进行排序
data3=models.User.objects.order_by('age')

# 多项排序
data4=models.User.objects.order_by('age','id')

# 逆向排序
data5=models.User.objects.order_by('-age')        #逆向排序就是在条件的前面加个负号

# 将返回来的QuerySet中的Model转换为字典
data6=models.User.objects.all().values()

# 获取当前查询到的数据的总数
data7=models.User.objects.count()

'''
常用的查询条件：
        查找对象的条件的意思是传给以上方法的一些参数。
        相当于是SQL语句中的where语句后面的条件，语法为字段名__规则(是连着连个下划线哦)
'''
'''查询条件'''
# exact:相当于等于号(name='辣椒')，准确查询
result=models.User.objects.filter(name__exact='辣椒')
print(result)
# contains:包含,里面包含了什么东西,字段名name包含了‘小’字
result1=models.User.objects.filter(name__contains='小')
print(result1)
# startwith:以什么开始
result2=models.User.objects.filter(name__startwith='小')
# endwith:以什么结尾
result3=models.User.objects.filter(name__endwith='q')
# istartswith:同startwith,忽略大小写；iendswith:同endwith,忽略大小写
result4=models.User.objects.filter(name__istartwith='fzq')
# in:成员所属，18或者21
resul5t=models.User.objects.filter(age__in=[18,21])
# range:范围所属，区间：18,19,20
result6=models.User.objects.filter(age__range=(18,20))
# gt:大于
result7=models.User.objects.filter(age__gt=20)
# gte:大于等于
result8=models.User.objects.filter(age__gte=20)
# lt:小于
result9=models.User.objects.filter(age__lt=20)
# lte:小于等于
result0=models.User.objects.filter(age__lte=20)
# isnull:判断是否为空
result11=models.User.objects.filter(name__isnull='辣椒')
"""
from .models import Ftest
def add_ftest(request):
    # 添加数据
    # Ftest.objects.create(name='fzq', age=21,note='我是fzq小弟')
    # ft=Ftest(name='GG',age=21,note='哈哈哈')
    # ft.save()
    # 查询+修改数据
    # f1=Ftest.objects.get(name='辣椒')   #返回的是单个实例
    # f1.note='我是假辣椒'
    # f1.save()
    f2=Ftest.objects.filter(name='狒狒') #返回的是QuerySet对象
    print(f2)
    # f2.update(name='小付fff')
    # f2.note='你好'
    # f2.save()
    '''更改失败，不能这样修改的，必须先获取，在filter()[0]获取，再更改'''
    f2[0].note='大神的'
    f2[0].save()
    return HttpResponse('成功')

