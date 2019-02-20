from django.shortcuts import render

# Create your views here.
#  常用的模板标签
def template_tag(request,haha):
    context={
        'name':'fff',
        'list':[1,2,3],
        'list1':[0,9,8],
        'num1':12,
        'num2':34,
    }

    return render(request,'04/04_index_01.html',context=context)
# 标签url跳转的函数
def index_04(request,haha):
    return render(request,'04/04_index_02.html')



'''
模板继承使用extends标签实现。通过使用block来给子模板开放接口。
1、extends必须是模板中的第一个出现的标签。
2、子模板中的所有内容，必须出现在父模板定义好的block中，否则django将不会渲染。
3、如果出现重复代码，就应该考虑使用模板。
4、尽可能多的定义block，方便子模板实现更细的需求。
5、如果在某个block中，要使用父模板的内容，使用block.super获取。
'''
# 模板继承与引用
def index_05(request):
    return render(request,'04/04_index_03.html')


# 自定义过滤器
def index_06(request):
    return render(request,'04/自定义过滤器.html',context={'str':'ASDFFG'})

# 自定义标签
import datetime
def index_07(request):
    context={'name':'fzq',
             'now':datetime.datetime.now(),
             'format_time':'%Y年%m月%d日：%H：%M:%S',
             'list':[1,2,3,4,5],
             'tuple':('哈哈哈','呵呵呵','嘻嘻嘻','嘿嘿嘿')}
    return render(request,'04/自定义标签.html',context=context)