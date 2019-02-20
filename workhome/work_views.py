from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
# Create your views here.

# 1.用int转换器
def hello(request,name,age):
    return HttpResponse('hello,%s大哥,去年%d岁'%(name,age))

# 2.使用reverse,redirect实现页面跳转
def page(request):
    return redirect(reverse('new_page'))
def page2(request):
    return HttpResponse('新页面')

# 3.使用render渲染模板
def index(request):
    return render(request,'workhome/index.html')