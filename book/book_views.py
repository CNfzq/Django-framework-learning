from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# Create your views here.

def book_index(request,**kwargs):
    print(kwargs)
    return HttpResponse('这是book首页',)

def book_test(request,**kwargs):
    print(kwargs)
    return HttpResponse('book_test',kwargs)

'''-------------以下两个函数测试页面跳转----------------'''
def article(request,name):
    return redirect(reverse('new_article',args=(name,)))
    # return redirect('/book/article_new')
    # return HttpResponse('这是老的界面')
def article_new(request,name):

    return HttpResponse('这是新的界面')


'''HttpResponse只是编码，只是把字符串编码出去，发送到浏览器界面。还有其他方法能够发送到浏览器界面,比如render()方法，还有get_remplate()方法'''
from django.template.loader import get_template   #导入get_template()方法：用于获取模板

'''-------------以下两个函数测试模板渲染----------------'''
def get_temp(request):
    temp=get_template('book/index.html')        #最麻烦的一种方法，不用
    html=temp.render()
    return HttpResponse(html)

# render方法是django封装好用来渲染模板的方法很方便
def index(request):
    name='hahahahahahah'    #自定义一个参数，可以传别的参数进来
    return render(request, 'book/index.html',context=name) #使用简便的方法，第一个参数request是请求对象，也就是传入的request，第二个参数是模板文件,第三个参数是传参(字典形式)，传给模板里面的参数，模板一般用{{}}接收

'''一般在templates文件夹里各自新建自己的模板文件，比如：book需要的模板就建一个book文件夹来管理自己的模板，这样防止模板的冲突'''
